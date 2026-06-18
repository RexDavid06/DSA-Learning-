# Create a Student class
''' Requirements
    Instance Attributes
        name
        age
    Class Attributes
        school = 'Madonna University'
    
        then create two student objects

'''

class Student:
    school = 'Madonna University'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student('Kelly', 25)
student2 = Student('Ekwe', 24)

print(student1.name)
print(student2.name)
print(Student.school)
    



