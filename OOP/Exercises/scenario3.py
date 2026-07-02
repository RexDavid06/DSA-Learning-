'''

Scenario 3: Gym Management System
Given your fitness background:

Member
Trainer
WorkoutPlan
Exercise

Could you model the relationships between these classes?

'''

import uuid
class Exercise:
    def __init__(self, name, muscle_group):
        self.name = name
        self.muscle_group = muscle_group

    def exercise_anmimation(self):
        print(f"The {self.name} exercise is done this way..... 😊😊")
    


class WorkoutPlan:
    def __init__(self, day, exercise):
        self.day = day
        self.exercise = exercise

class Member:
    total = 0
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        Member.total += 1

class Client(Member):
    total = 0
    def __init__(self, username, email, password):
        client_id = uuid.uuid4()
        super().__init__(username, email, password)
        self.client_id = client_id
        Client.total += 1


class Trainer(Member):
    total = 0
    def __init__(self, username, email, password):
        trainer_id = uuid.uuid4()
        super().__init__(username, email, password)
        self.trainer_id = trainer_id
        Trainer.total += 1
    

exercise1 = Exercise('Over head tricep extensions', 'Triceps')
exercise2 = Exercise('Barbell back squat', 'Quadriceps')
exercise3 = Exercise('Incline bench press', 'Percs')
workoutplan1 = WorkoutPlan('Mon', exercise1)
workoutplan2 = WorkoutPlan('Tues', exercise2)
client1 = Client('tosin', 'tosin@gmail.com','tosin123')
client2 = Client('mabel', 'mabel@gmail.com','mabel123')
trainer1 = Trainer('dubem', 'dubem@gmail.com', 'dubem123')
trainer2 = Trainer('malik', 'malik@gmail.com', 'malik123')

print(exercise1.__dict__)
print(workoutplan1.__dict__)
print(f"We have a total of {Member.total} members")
print(f"We have a total os {Client.total} clients")
print(f"We have a total of {Trainer.total} trainers")
print(trainer1.trainer_id)
print(trainer2.trainer_id)
print(client1.client_id)
print(client2.client_id)