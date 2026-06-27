# Polymorphism
# Polymorphism in Python refers to the ability of different object types to respond to the same function name,
# method name, or operator in their own unique way. Derived from Greek meaning "many forms", it allows 
# developers to use one unified interface to control multiple unique implementations, eliminating repetitive 
# conditional logic (like if-elif type checks) and making code highly scalable.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year

    def start(self):
        print('Vehicle is starting....')
    
    def stop(self):
        print('Vehicle is stopping....')


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
    
    #This methods override the start and stop methods in the parent class, for more control in the class inheriting
    def start(self):
        print('Car is starting....')
    
    def stop(self):
        print('Car is stopping....')


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
    
    #This methods override the start and stop methods in the parent class, for more control in the class inheriting
    def start(self):
        print('Motorcycle is starting....')
    
    def stop(self):
        print('Motorcycle is stopping....')



vehicles = [
    Car('Ford', 'Raptor', 2019, 4),
    Motorcycle('Honda', 'Scoopy', 2018),
    Car('Hyundai', 'Aua', 2030, 2),
    Motorcycle('Tesla', 'petty', 2027),
]

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("This isn't a valid vehicle....")


# DISPITE THE DIFFERENT VEHICLE CLASS, POLYMORPHISM ALLOWS US TO TREAT THEM AS INSTANCES OF THE BASE VEHICLE CLASS
