'''
What I'd challenge you with next

Now you're ready for something bigger.

Build this.

Bank
│
├── Customer
│      │
│      ├── SavingsAccount
│      └── CurrentAccount
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
    def __init__(self, name):
        self.name = name 
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_customers(self):
        return self.customers


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.accounts = []
    
    def show_detail(self):
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

    @property
    def balance(self):
        return self._balance

class SavingsAccount:
    pass
        

class CurrentAccount:
    pass

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