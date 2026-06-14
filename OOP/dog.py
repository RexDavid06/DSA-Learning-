class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print('woof woof')

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name 
        self.address = address
        self.phone_number = contact_number

owner1 = Owner('Sally', '123 calvary drive', '555-666')
dog1 = Dog('Mary', 'WolfBarne', owner1)
print(dog1.owner.address)
