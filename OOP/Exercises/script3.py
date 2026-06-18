'''Exercise 3: Static Method (Basic)

Create a Calculator class.

Requirements:

Create static methods:

add(a, b)
subtract(a, b)
multiply(a, b)

Example:

print(Calculator.add(2, 5))
print(Calculator.multiply(4, 6))'''

class Calculator:

    @staticmethod
    def add(a, b):
        result = a + b
        return result

    def subtract(num1, num2):
        result = num1 - num2
        return result

    def multiply(num1, num2):
        result = num1 * num2
        return result
    

print(Calculator.multiply(10, 50))


