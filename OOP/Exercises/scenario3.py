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

    def exercise_animation(self):
        print(f"The {self.name} exercise is done this way..... 😊😊")
    


class WorkoutPlan:
    def __init__(self, day):
        self.day = day
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    
        


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
        self.workoutplans = []
        Client.total += 1

    def show_workouts(self):
        if not self.workoutplans:
            return 'No workout today'
        
        for plan in self.workoutplans:
            print(f"Woekout plan for {plan.day}")
            for exercise in plan.exercises:
                print(f"Exercise: {exercise.name} for {exercise.muscle_group}")            



class Trainer(Member):
    total = 0
    def __init__(self, username, email, password):
        trainer_id = uuid.uuid4()
        super().__init__(username, email, password)
        self.trainer_id = trainer_id
        Trainer.total += 1
    
    def assign_workout(self, client, workout_plan):
        client.workoutplans.append(workout_plan)
    

exercise1 = Exercise('Over head tricep extensions', 'Triceps')
exercise2 = Exercise('Barbell back squat', 'Quadriceps')
exercise3 = Exercise('Incline bench press', 'Pectoral')
workoutplan1 = WorkoutPlan('Mon')
workoutplan1.add_exercise(exercise1)
workoutplan1.add_exercise(exercise2)
workoutplan2 = WorkoutPlan('Tues')
workoutplan2.add_exercise(exercise3)
client1 = Client('tosin', 'tosin@gmail.com','tosin123')
client2 = Client('mabel', 'mabel@gmail.com','mabel123')
trainer1 = Trainer('dubem', 'dubem@gmail.com', 'dubem123')
trainer2 = Trainer('malik', 'malik@gmail.com', 'malik123')


print(f"We have a total of {Member.total} members")
print(f"We have a total os {Client.total} clients")
print(f"We have a total of {Trainer.total} trainers")
print(trainer1.trainer_id)
print(trainer2.trainer_id)
print(client1.client_id)
print(client2.client_id)