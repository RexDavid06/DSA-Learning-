'''
Composition is a design principle in object-oriented programming (OOP) where a class is constructed using 
instances of other classes as attributes to build complex behavior. It models a "has-a" relationship 
(or "part-of" relationship) rather than the "is-a" relationship modeled by traditional inheritance.

'''

class Engine:
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS an Engine

    def drive(self):
        self.engine.start()
        print("Car is moving.")


car = Car()
car.drive()


class Phone:
    def call(self):
        print("Calling...")


class Person:
    def __init__(self, name):
        self.name = name
        self.phone = Phone()   # Person HAS a Phone

    def make_call(self):
        print(f"{self.name} is making a call.")
        self.phone.call()


rex = Person("Rex")
rex.make_call()


class Keyboard:
    def type(self):
        print("Typing...")


class Computer:
    def __init__(self):
        self.keyboard = Keyboard()

    def work(self):
        self.keyboard.type()


pc = Computer()
pc.work()