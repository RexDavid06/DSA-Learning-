a = 5
b = 10

def my_function():
    global a 
    """"the keyword global  refers to the global variable a... i.e  
    if any change is made to the variable a, it should affect 
    the global variable a """
    a = 6; b = 15

my_function()
print(a)
print(b)


