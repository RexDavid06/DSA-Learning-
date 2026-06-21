# Inheritance is a fundamental concept in Object Oriented Programming that involves creating new classes...
#  (Subclasses or Derived classes based) on existing classes (superclasses or base classes)

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('Vehicle is starting....')
    
    def stop(self):
        print('Vehicle is stopping...')
        

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels, type_of_fuel):
        'the super method calls the init method of the parent class(Vehicle)'
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels
        self.type_of_fuel = type_of_fuel


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels


car1 = Car('Ford', 'Focus', 2008, 4, 4, 'Diesel')

bike1 = Bike('Honda', 'Scoopy', 2018, 2)

print(car1.__dict__)
bike1.start()