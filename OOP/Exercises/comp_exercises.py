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
        def __init__(self, number_of_rooms):
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
   def __init__(self, name):
        self.name = name

   def flying(self):
        print(f"{self.name} is flying")
   
   def walking(self):
        print(f"{self.name} is walking")


class Eagle(Bird):
   def __init__(self, name, specie, color):
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
     def __init__(self, brand, color):
          self.brand = brand
          self.color = color
          self.battery = Battery()


lappy = Laptop('HP', 'Black')
print(lappy.__dict__)


# 4. Employee - Manager

class Manager:
     pass

class Employee:
     def __init__(self, name):
          self.name = name 
          self.manager = Manager()