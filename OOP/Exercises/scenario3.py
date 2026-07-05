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


class WorkoutPlan:
    def __init__(self, day):
        self.day = day
        self.exercises = []
    
    def add_exercises(self, exercise):
        self.exercises.append(exercise)
        return f"{exercise.name} has been added to your workout list"

    # def __str__(self):
    #     return f"Day: {self.day} \n Exercises: {self.exercises}"


class Member:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Client(Member):
    def __init__(self, username, email, password):
        client_id = str(uuid.uuid4())
        super().__init__(username, email, password)
        self.client_id = client_id
        self.workout_plans = []
    
    def __str__(self):
        return self.workout_plans

    def show_workouts(self):
        if not self.workout_plans:
            return f"No workout plan today"
        
        for plan in self.workout_plans:
            print(f"Workout Plan for {plan.day}")
            for exercise in plan.exercises:
                print(f"{exercise.name} - {exercise.muscle_group}")


class Trainer(Member):
    def __init__(self, username, email, password):
        trainer_id = str(uuid.uuid4())
        super().__init__(username, email, password)
        self.trainer_id = trainer_id

    def assign_workout(self, client, workout_plan):
        client.workout_plans.append(workout_plan)


exercise1 = Exercise('Over head tricep extension', 'Triceps')
exercise2 = Exercise('Bulgarian Split Squat', 'Quadriceps')

workout_plan1 = WorkoutPlan('Monday')
workout_plan2 = WorkoutPlan('Wednesday')


client1 = Client('Tosin', 'tosin@gmail.com', 'tosin123')
client2 = Client('Chidi', 'chidi@gmail.com', 'chidi123')

trainer1 = Trainer('Dubem', 'dubem@gmail.com', 'dubem123')
trainer2 = Trainer('Mechanic', 'mechanic@gmail.com', 'mechanic123')

workout_plan1.add_exercises(exercise1)
workout_plan1.add_exercises(exercise2)

# for plan in workout_plan1.exercises:
#     print(plan.name)


trainer1.assign_workout(client1, workout_plan1)
client1.show_workouts()