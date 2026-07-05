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
class Bank:
    pass

class Customer:
    pass

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