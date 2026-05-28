# Count the number of vowels

x = 'MathemAtIcs'
vowels = ['a', 'e', 'i', 'o', 'u']
output = 0

#firstly, iterate over the letters in the variable x
for char in x:
    #then while the letters are converted to lower cases, check if they appear in the vowels variable.
    if char.lower() in vowels:
        # If they do, add a count to the outpt variable representing the number of vowels in the x variable.
        output += 1

print(output)

