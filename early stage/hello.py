
name = input("What is your name? ")

#the .strip method removes whitespaces from a text, 
# the .capitalize capitalizes the first letter  of the first word in a sentence

name = name.strip().capitalize()
print(f"Hello {name}")
print("")

#the  title method capitalizes the first letter of every word in a sentence
name = name.strip().title()
print(f"welcome {name}")
print("")

# the split method seperates the words in a sentence.
first, last = name.split()
print(f"splitted {first}")