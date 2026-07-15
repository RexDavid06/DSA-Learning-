
print('Welcome to the calculator')
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    print(subtract(90, 10))


'So, if i run the file directly, the subtract function will be called, but if i run this file externally '
'from another script,it then does nothing But the print statement will be called regardless....'
'both internally and externally(if the calculator module is imported)'

# Reference to the main.py file in this directory!!