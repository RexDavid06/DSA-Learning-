# Encapsulation
# ''' Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, such as a class.
#  It restricts direct access to some of an object's components, which can prevent the accidental modification of data.
#  In Python, we can achieve encapsulation using private and protected members. '''



class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__balance = 0.0

    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount <= 0:
            return ValueError('Amount should be greater than 0')
        self.__balance += amount
        return self.__balance
        

    def withdraw(self, amount):
        if amount > self.__balance:
            return ValueError('Insufficient Fund')
        self.__balance -= amount
        return self.__balance
    

account1 = BankAccount('Alice')
print(account1.deposit(600))
print(account1.withdraw(300))
print(account1.balance)



 