'''Exercise 8: E-commerce Discount

Create a Product class.

Requirements:

Instance attributes:

name
price

Static method:

apply_discount(price, percentage)

Example:

print(Product.apply_discount(10000, 20))

Expected output:

8000

Expected understanding:

Static methods that transform values.'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def apply_discount(price, percentage):
        discounted_amount = (percentage/100) * price
        payment_after_discount = price - discounted_amount
        return f'The product price is {price} but new price after the {percentage}% discount, is {payment_after_discount}'
        

product1 = Product('Iphone 11', 300000)
print(Product.apply_discount(product1.price, 15))
