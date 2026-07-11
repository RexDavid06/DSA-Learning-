'''
Part 2: Reading Files

Create a file named:

students.txt

Content:

John
Mary
David
Sarah
James
Exercise 5

Read the file and print every student's name.

Exercise 6

Print the total number of students.

Expected:

Total students: 5
Exercise 7

Print only names that start with "J".

Expected:

John
James
Exercise 8 (Challenge)

Print the names alphabetically.
'''

# Exercise 5
with open('student.txt', 'r') as rf:
    rf_contents = rf.read()
    print(rf_contents)

# Exercise 6
with open('student.txt', 'r') as rf:
    total_number_of_students = 0
    for line in rf:
        total_number_of_students += 1
    print(f"Total students: {total_number_of_students}")

# Exercise 7
with open('student.txt', 'r') as rf:
    for line in rf:
        if line.startswith('J'):
            print(line, end='')

# Exercise 8
with open('student.txt', 'r') as f:
    students = f.readlines()
    students.sort()
    for student in students:
        print(student, end='')