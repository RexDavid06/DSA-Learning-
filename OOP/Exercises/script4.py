'''Exercise 4: Temperature Converter

Create a TemperatureConverter class.

Create static methods:

celsius_to_fahrenheit(c)
fahrenheit_to_celsius(f)

Formula:

F = (C × 9/5) + 32
C = (F − 32) × 5/9

Example:

print(TemperatureConverter.celsius_to_fahrenheit(30))

Expected understanding:

Static methods used as utility functions.'''

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        f = (c * 9/5) + 32
        return f'{f} F'
    
    def fahrenheit_to_celcius(f):
        c = (f - 32) * 5/9
        return f'{c} C'


print(TemperatureConverter.celsius_to_fahrenheit(30))
print(TemperatureConverter.fahrenheit_to_celcius(86))