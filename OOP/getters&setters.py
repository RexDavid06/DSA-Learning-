#Two major ways of Getting and Setting data on an object.

# 1. Traditional way: make the data private and use getters and setters.

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email


user1 = User('moon', 'moon@gmail.com', 'password123')

user1.set_email('newemail@gmail.com')
print(user1.get_email())


# 2. Using the @property decorator

class Dog:
    def __init__(self, breed, name, color):
        self.breed = breed
        self.name = name
        self.__color = color

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color



dog1 = Dog('german sheperd', 'Whisky', 'black')
dog1.color = 'rED'
print(dog1.color)

