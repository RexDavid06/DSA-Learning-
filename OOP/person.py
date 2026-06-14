class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, i'm {self.name} and i'm {self.age} years old")

person1= Person('Amanda', 90)
person1.greet()
