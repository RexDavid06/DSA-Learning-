'''
Part 3: Writing Files
Exercise 9

Create a file called

shopping.txt

Write:

Rice
Beans
Milk
Bread
Exercise 10

Ask the user:

Enter another item:

Append it to the file.

(Hint: Use append mode.)

Exercise 11

Read the file again and display everything.
'''

# Exercise 9
with open('shopping.txt', 'w') as wf:
    wf.write('Rice\nBeans\nMilk\nBread\n')

# Exercise 10
with open('shopping.txt', 'a') as af:
    item = input('Enter another item: ')
    af.write(item + '\n')

# Exercise 11
with open('shopping.txt', 'r') as f:
    f_content = f.read()
    print(f_content)