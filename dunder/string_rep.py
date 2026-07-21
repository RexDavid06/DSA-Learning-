''' 
'''
class Student:
    def __init__(self, name:str, age:int, department:str):
        self.name = name 
        self.age = age
        self.department = department
    
    def __repr__(self) -> str:
        return f"{self.name} {self.age} {self.department}"



object1 = Student('Angel', 20, 'mechanical')

print(object1)
# print(str(object1))
# print(repr(object1))

