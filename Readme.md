This interactive banking system allows users to create accounts, deposit and withdraw money, transfer funds, and display account balances. The system uses Object-Oriented Programming principles, including classes for users and account types with specific methods for managing transactions.
I'm going to give a little description of my classes
User:
Represents a bank user with attributes for user_id, name, and a list of accounts.
Methods:
add_account(): Adds an account to the user's account list.
display_accounts(): Displays the user's accounts and their balances.

BankAccount (Abstract Base Class):
Defines the blueprint for a bank account with an account number and balance.
Methods:
deposit(): Adds funds to the account balance.
withdraw(): Abstract method for withdrawal, implemented in subclasses.
get_balance(): Retrieves the account balance.

SavingsAccount (Inherits from BankAccount):
Represents a savings account with withdrawal constraints.
Implements withdraw(), checking if there’s sufficient balance before allowing a withdrawal.

CheckingAccount (Inherits from BankAccount):
Represents a checking account with an overdraft limit.
Implements withdraw() with overdraft capability, allowing balance to go negative up to the overdraft limit.
This system integrates the classes into a user-friendly menu-driven interface, enabling basic banking operations interactively.

Key OOP Concepts portrayed are:
Encapsulation: Certain attributes, like balance, are private and accessed through getter and setter methods.
Inheritance: SavingsAccount and CheckingAccount inherit from BankAccount.
Polymorphism: Methods like withdraw() and deposit() are overridden in subclasses to implement different behavior.
Abstraction: We'll use an abstract class BankAccount that defines the structure for account-related functionality.






