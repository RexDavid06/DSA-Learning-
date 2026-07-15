'''
Scenario 1: Banking App
Account
├── SavingsAccount
├── CurrentAccount

Requirements:

deposit()
withdraw()
transfer()

Each account type has different withdrawal rules.

Could you model that using inheritance and polymorphism?
'''
import random

class Account:
    def __init__(self, name: str):
        # Generates a valid 10-digit account string
        self.account_number = str(random.randint(1000000000, 9999999999))
        self.name = name
        self.balance = 0.0

    def deposit(self, amount:int) -> str:
        if amount <= 0:
            return "Deposit must be greater than 0."
        self.balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount: int) -> str:
        """Base withdrawal method to be overridden by child classes."""
        if amount <= 0:
            return "Withdrawal must be greater than 0."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def transfer(self, amount, receiver_account):
        pass #I need help!! 


class SavingsAccount(Account):
    def __init__(self, name: str):
        super().__init__(name)
        # Savings rule: cannot go below a minimum balance
        self.min_balance = 500.0
        self.balance = 500.0  # Starting bonus to avoid immediate lock

    def withdraw(self, amount: int) -> str:
        """Overrides parent to enforce a minimum balance safety net."""
        if amount <= 0:
            return "Withdrawal must be greater than 0."
        if self.balance - amount < self.min_balance:
            return f"Denied. Savings Account must maintain a ${self.min_balance} minimum balance."
        
        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"


class CurrentAccount(Account):
    def __init__(self, name: str):
        super().__init__(name)
        # Current rule: allows overdraft up to a certain limit
        self.overdraft_limit = 1000.0

    def withdraw(self, amount: int) -> str:
        """Overrides parent to allow spending into a negative balance."""
        if amount <= 0:
            return "Withdrawal must be greater than 0."
        if self.balance - amount < -self.overdraft_limit:
            return f"Denied. Exceeds overdraft limit of ${self.overdraft_limit}."
        
        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
