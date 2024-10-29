from abc import ABC, abstractmethod

#User class
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        """Adds a bank account to the user's account list."""
        self.accounts.append(account)

    def display_accounts(self):
        """Displays all accounts associated with the user."""
        print(f"\nUser {self.name} has the following accounts:")
        for account in self.accounts:
            print(f" - {account.account_type} Account with balance: {account.get_balance()}")

#Abstract BankAccount Class
class BankAccount(ABC):
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self._balance = initial_balance
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance is {self._balance}")

    @abstractmethod
    def withdraw(self, amount):
            pass
    def get_balance(self):
            return self._balance
        
#SavingsAccount class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0):
        super().__init__(account_number, initial_balance)
        self.account_type = "Savings"
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance in savings account.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

#CheckingAccount class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=500):
        super().__init__(account_number, initial_balance)
        self.account_type = "Checking"
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

#Transaction class
class Transaction:
    @staticmethod
    def transfer(sender_account, receiver_account, amount):
        if sender_account.get_balance() < amount:
            print("Insufficient funds for transfer.")
        else:

            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
            print(f"Transferred {amount} from {sender_account.account_type} to {receiver_account.account_type}.")

#Main function
def main():
    users = {}

    def create_user():
        user_id = input("User ID: ")
        name = input("Name: ")
        users[user_id] = User(user_id, name)
        print(f"User {name} created.")

    def create_account(user):
        acc_type = input("Account type (Savings/Checking): ").strip().lower()
        acc_num = input("Account number: ")
        balance = float(input("Initial balance: "))
        
        if acc_type == "savings":
            account = SavingsAccount(acc_num, balance)
        elif acc_type == "checking":
            overdraft = float(input("Overdraft limit: "))
            account = CheckingAccount(acc_num, balance, overdraft)
        else:
            print("Invalid account type.")
            return

        user.add_account(account)
        print(f"{acc_type.capitalize()} account created.")

    def deposit(user):
        account = select_account(user)
        if account:
            amount = float(input("Deposit amount: "))
            account.deposit(amount)

    def withdraw(user):
        account = select_account(user)
        if account:
            amount = float(input("Withdraw amount: "))
            account.withdraw(amount)

    def select_account(user):
        for idx, acc in enumerate(user.accounts):
            print(f"{idx + 1}. {acc.account_type} - Balance: {acc.get_balance()}")
        choice = int(input("Select account: ")) - 1
        return user.accounts[choice] if 0 <= choice < len(user.accounts) else None

    while True:
        print("\n1. Create User\n2. Create Account\n3. Deposit\n4. Withdraw\n5. Display Accounts\n6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_user()
        elif choice == "2":
            user_id = input("User ID: ")
            user = users.get(user_id)
            if user: create_account(user)
            else: print("User not found.")
        elif choice == "3":
            user_id = input("User ID: ")
            user = users.get(user_id)
            if user: deposit(user)
            else: print("User not found.")
        elif choice == "4":
            user_id = input("User ID: ")
            user = users.get(user_id)
            if user: withdraw(user)
            else: print("User not found.")
        elif choice == "5":
            user_id = input("User ID: ")
            user = users.get(user_id)
            if user: user.display_accounts()
            else: print("User not found.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

# Run the interactive system
if __name__ == "__main__":
    main()
