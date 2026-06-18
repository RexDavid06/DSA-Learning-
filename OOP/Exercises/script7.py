'''Exercise 7: Bank Charges

Create a BankAccount class.

Requirements:

Instance attributes:

owner
balance

Static method:

calculate_transfer_fee(amount)

Rule:

Transfers below ₦5,000 → ₦10 fee
₦5,000–₦50,000 → ₦25 fee
Above ₦50,000 → ₦50 fee

Example:

print(BankAccount.calculate_transfer_fee(3000))
print(BankAccount.calculate_transfer_fee(20000))

Expected understanding:

Using static methods for business rules.'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def calculate_transfer_fee(amount):
        if amount < 5000:
            return f'Transfer fee is #10'
        elif 5000 >= amount < 50000:
            return f'Transfer fee is #25'
        else:
            return f'Transfer fee is #50'

account1 = BankAccount('Angel', 9000)
print(account1.calculate_transfer_fee(4999))
