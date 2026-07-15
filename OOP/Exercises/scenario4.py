'''
What I'd challenge you with next

Now you're ready for something bigger.

Build this.

Bank
│
├── Customer
|       |
|       |__Account
|             |
│             │
│             ├── SavingsAccount
│             └── CurrentAccount
│
├── Transaction
│
├── TransferService
│
├── TransferValidator
│
└── TransactionHistory

Where:

Every transfer creates a Transaction.
Every account stores its transaction history.
TransferService handles the transfer logic.
TransferValidator validates limits, balances, and account status.
Account should not perform transfers directly.

This introduces composition, which is even more common than inheritance in real backend systems.

'''

import random
import uuid
class Bank:
    def __init__(self, name: str):
        self.name = name 
        self.customers = []

    def add_customer(self, customer: str) -> None:
        self.customers.append(customer)

    def view_customers(self) -> list:
        return self.customers


class Customer:
    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address
        self.accounts = []
    
    def show_detail(self) -> str:
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}"
    
    def add_accounts(self, account):
        self.accounts.append(account)
    
    def show_all_accounts(self):
        return self.accounts

    

class Account:
    def _init__(self):
        account_number = random.randint(1000000000, 9999999999)
        self.account_number = account_number
        self._balance = 0.0
        self.transactions = []

    @property
    def balance(self) -> int|float:
        return self._balance

    def deposit(self, amount: int|float) -> str:
        if amount < 100:
            return f"Amount should be more than 100."
        else:
            self._balance += amount
            return f"{amount} credited to balance"

    
    def withdraw(self, amount: int|float) -> str:
        if amount < 100:
            return f"Amount should be more than 100."
        if self._balance < amount:
            return f"You have insufficient funds for this transaction."
        else:
            self._balance -= amount
            return f"{amount} debited from balance"

    def add_transactions(self, transaction):
        self.transactions.append(transaction)
    
    def view_transactions(self) -> list:
        return self.transactions



class SavingsAccount(Account):
    MIN_BALANCE = 500
    def __init__(self, name):
        self.name = name  

    def withdraw(self, amount):
        if self._balance <= self.MIN_BALANCE:
            return f"500 should be the minImum amount left in the account."
        if self._balance < amount:
            return f"You have insufficient funds for this transaction." 
        else:
            self._balance -= amount    

class CurrentAccount(Account):
    def __init__(self, name):
        self.name = name


class Transaction:
    pass

class TransferService:
    pass

class TransferValidator:
    pass

class TransferHstory:
    pass



customer1 = Customer('Alice', 'alice@gmail.com', 'PH, Nigeria')
bank1 = Bank('United Bank Of Africa')
bank1.add_customer(customer1)
print(customer1.name)
print(bank1.name)

for char in bank1.customers:
    if char.accounts == []:
        print(f"{char.name} has no Acccounts Yet!!'")
    else:
        print(char.accounts)