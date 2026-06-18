'''Exercise 6: Circle

Create a Circle class.

Requirements:

Instance attribute:
radius
Static method:
calculate_area(radius)

Formula:

π × radius²

Example:

c = Circle(5)

print(Circle.calculate_area(c.radius))

Expected understanding:

Combining objects with static methods.'''
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def calculate_area(radius):
        result = pi * (radius ** 2)
        return result
    
c = Circle(5)
print(Circle.calculate_area(c.radius))