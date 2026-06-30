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