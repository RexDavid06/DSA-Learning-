'''Exercise 10 (Mini Project)

Build a simple ATM class.

Requirements:

Instance attributes:

owner
balance

Methods:

deposit(amount)
withdraw(amount)

Static method:

is_valid_pin(pin)

Rules:

PIN is valid if:

Exactly 4 digits.
Contains only numbers.

Example:

ATM.is_valid_pin("1234")
ATM.is_valid_pin("12a4")

This exercise combines everything you've learned so far.'''

class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'New Balance: {self.balance}'
    
    def wihtdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'New Balance: {self.balance}'
        
    @staticmethod
    def is_valid_pin(pin):
        if len(pin) == 4:
            if pin.isdigit():
                return f'{pin} is a valid pin'
        return f'{pin} is not a valid pin'



bank1 = ATM('Alice', 9000)
print(bank1.deposit(1000))
print(bank1.wihtdraw(5000))

    
