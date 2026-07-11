'''
Part 5: Combine OOP + Files
Exercise 12

Create a

class Student

Attributes:

name
age
course

Method:

save()

Save the student's details into

students.txt
Exercise 13

Create three Student objects.

Save them all to the same file.

Expected file:

John,20,Computer Science
Mary,19,Mechanical Engineering
David,22,Civil Engineering
Exercise 14

Read the file.

Convert every line back into information and print:

Name: John
Age: 20
Course: Computer Science
'''
# Exercise 12
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def save(self):
        with open('students.txt', 'a') as af:
            af.write(f"{self.name}, {self.age}, {self.course}\n")



student1 = Student('John',20,'Computer Science')
student2 = Student('Mary',19,'Mechanical Engineering')
student3 = Student('David',22,'Civil Engineering')

# Exercise 13
student1.save()
student2.save()
student3.save()

# Exercise 14
with open('students.txt', 'r') as rf:
    for line in rf:
        'using sequence unpacking'
        name, age, course = line.strip().split(',')
        print(f"Name: {name}\nAge: {age}\nCourse: {course}\n")
    

