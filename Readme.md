This interactive banking system allows users to create accounts, deposit and withdraw money, transfer funds, and display account balances. The system uses Object-Oriented Programming principles, including classes for users and account types with specific methods for managing transactions.
I'm going to give a little description of my classes
User:
Represents a bank user with attributes for user_id, name, and a list of accounts. Holds information about the user and their accounts. It manages the user's accounts, allowing them to view and add new accounts.
Methods:
add_account(): Adds an account to the user's account list.
display_accounts(): Displays the user's accounts and their balances.

BankAccount (Abstract Base Class):
Defines the blueprint for a bank account with an account number and balance. An abstract base class that provides common behavior for all accounts, like depositing and balance checking.
Methods:
deposit(): Adds funds to the account balance.
withdraw(): Abstract method for withdrawal, implemented in subclasses.
get_balance(): Retrieves the account balance.

SavingsAccount (Inherits from BankAccount):
Represents a savings account with withdrawal constraints. A specific type of bank account with a withdrawal method that ensures no overdraft.
Implements withdraw(), checking if there’s sufficient balance before allowing a withdrawal.

CheckingAccount (Inherits from BankAccount):
Represents a checking account with an overdraft limit. Allows overdrafts within a defined limit and handles withdrawals with this behavior.
Implements withdraw() with overdraft capability, allowing balance to go negative up to the overdraft limit.
This system integrates the classes into a user-friendly menu-driven interface, enabling basic banking operations interactively.

Transaction: Facilitates money transfers between different bank accounts.

Key OOP Concepts portrayed are:
Encapsulation: Certain attributes, like balance, are private and accessed through getter and setter methods.
Inheritance: SavingsAccount and CheckingAccount inherit from BankAccount.
Polymorphism: Methods like withdraw() and deposit() are overridden in subclasses to implement different behavior.
Abstraction: We'll use an abstract class BankAccount that defines the structure for account-related functionality.

Exception Handling
The system prevents withdrawing more than available funds (for Savings Account) or exceeding overdraft limits (for Checking Account).
It prevents transferring funds when the sender doesn't have enough balance.





