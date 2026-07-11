'''Part 1: join() Exercises
Exercise 1 (Easy)

Given:

fruits = ["Apple", "Banana", "Orange", "Mango"]

Print:

Apple, Banana, Orange, Mango
Exercise 2

Given:

letters = ['P', 'Y', 'T', 'H', 'O', 'N']

Print:

PYTHON
Exercise 3

Given:

words = ["Backend", "Developer", "Journey"]

Print:

Backend -> Developer -> Journey
Exercise 4 (Challenge)

Input:

sentence = "Python is awesome"

Output:

Python-is-awesome

(Hint: You'll need both split() and join().)
'''
# Exercise 1
fruits = ["Apple", "Banana", "Orange", "Mango"]
separator1 = ', '
joined1 = separator1.join(fruits)
print(joined1)

# Exercise 2
letters = ['P', 'Y', 'T', 'H', 'O', 'N']
separator2 = ''
joined2 = separator2.join(letters)
print(joined2)

# Exercise 3
words = ["Backend", "Developer", "Journey"]
separator3 = ' -> '
joined3 = separator3.join(words)
print(joined3)

# Exercise 4
sentence = "Python is awesome"
x = sentence.split()
separator4 = '-'
joined4 = separator4.join(x)
print(joined4)

