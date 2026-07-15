'''
Tiny Exercise for You

Without looking at the answer, tell me whether you'd use inheritance or composition for each:

House → Room
Bird → Eagle
School → Student
Laptop → Battery
Employee → Manager

Just reply like this:

1. Composition
2. Inheritance
3. ...

If you get all five right, you've understood the core idea behind composition.
'''

# 1 House - Room relationship
# the HOUSE-ROOM relationship is a "has-a" relationship. The house HAS-A room, so we're using composition

import uuid
class Room:
        def open_door(self):
           print('Opening Door.......')
        
        def close_door(self):
           print('Closing Door.......')

        def open_window(self):
              print('Opening Windows.....')
            
        def close_window(self):
              print('Closing Windows.....')


class House:
        def __init__(self, number_of_rooms: int):
            self.number_of_rooms = number_of_rooms
            self.room = Room()
    
        def domestic_maintenance(self):
             self.room.open_door()
             self.room.open_window()
             print('Running Maintenance now.....')
             print('Maintenace is done!!')
             self.room.close_window()
             self.room.close_door()


house1 = House(5)
house1.domestic_maintenance()

# 2. Bird - Eagle relationship
# the Bird and Eagle relationship is a "IS-A" relationship, the Eagle 'is a' Bird, so we're be using Inheritance

class Bird:
   def __init__(self, name: str):
        self.name = name

   def flying(self):
        print(f"{self.name} is flying")
   
   def walking(self):
        print(f"{self.name} is walking")


class Eagle(Bird):
   def __init__(self, name: str, specie: str, color: str):
          'we are calling the parent class constructor with the super method'
          super().__init__(name)
          self.specie = specie
          self.color = color

   def flying(self):
        print('Eagle is flying.....')

   def walking(self):
        print('Eagle is walking.....')
          
         
# ALSO LEVERAGING POLYMORPHISM

birds = [
     Bird('Kite'),
     Eagle('Eagle', 'Dessert Falcon', 'Black'),
     Bird('Sparrow'),
     Eagle('Eagle', 'Mountain Eagle', 'White'),
]

for bird in birds:
     if isinstance(bird, Bird):
          print(f"{bird.name} ({type(bird).__name__})")
          bird.walking()
          bird.flying()



# 3. Laptop - Battery Relationship 

class Battery:
     def charging(self):
          print('Battery is charging......')

     def dead(self):
          print('Battery just died....')


class Laptop:
     def __init__(self, brand: str, color: str):
          self.brand = brand
          self.color = color
          self.battery = Battery()


lappy = Laptop('HP', 'Black')
print(lappy.__dict__)


# 4. Employee - Manager
# The Employee and Manager relationship is s 'IS-A' relationship because a manager is alos an employee, but specialized employee

class Employee:
     def __init__(self, name: str, role: str, department: str):
          self.name = name 
          self.role = role
          self.department = department
          self.employee_id = uuid.uuid4()

     def annual_salary(self, salary: int|float) -> int|float:
          result = salary * 12
          return result
     
     def show_employee_id(self):
          return f"{self.name}'s employer ID: {self.employee_id}"



class Manager(Employee):
     def __init__(self, name: str, role: str, department: str, department_managing: str):
          super().__init__(name, role, department)
          self.department_managing = department_managing




emp = Employee('Jide', 'Customer Service', 'Marketing')
manager1 = Manager('Blessing', 'manager', 'Frontend Lead', 'Frontend Team')

print(manager1.annual_salary(30000))
print(manager1.show_employee_id())