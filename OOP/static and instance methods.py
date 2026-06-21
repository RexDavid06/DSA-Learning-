# Static methods in python are methods  that belong to the class itself rather than any instance of the class

# We define a static method by using  '@staticmethod' decorator

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance: ${self._balance}")
        else:
            print('Deposit amount must be positive')

    @staticmethod
    def is_valid_interest_rate(rate):
        if rate >= 0 and rate <= 5:
            return True
        else:
            return False

account1 = BankAccount('Alice', 500)
print(type(account1).__name__)

account1.deposit(200)
print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(90))