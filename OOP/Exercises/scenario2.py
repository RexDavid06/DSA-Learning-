'''
Scenario 2: E-commerce
Product
├── PhysicalProduct
├── DigitalProduct

Each product calculates shipping differently.

Could you use polymorphism to make:

product.calculate_shipping()

work differently depending on the product type?

'''

class Product:
    total_number_of_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_number_of_products += 1
    
    def calculate_shipping(self):
        'if the product price is less than 50,000, then the shpping fee will be 10% of the product price(Not real world Logic)'
        if self.price < 50000:
            shipping_fee = 10/100 * self.price
            total_payment = shipping_fee + self.price
            return f"The shipping fee for this product is {shipping_fee}\nThe Total payment is {total_payment}"
        else:
            shipping_fee = 20/100 * self.price
            total_payment = shipping_fee + self.price
            return f"The shipping fee for this product is {shipping_fee}\nThe Total payment is {total_payment}"
        
    

class PhysicalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)



class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
    

    def calculate_shipping(self):
        return f"Digital Products have no shipping fees\nSo total payment is {self.price}"



product1 = PhysicalProduct('Iphone 12', 300000)
product2 = DigitalProduct('WAEC result', 9000)


print(product1.calculate_shipping())
print(product2.calculate_shipping())
print(Product.total_number_of_products)