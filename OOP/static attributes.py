# Static Attributes
# A static attribute(class atribute) is an attribute that belongs to the class it self not to any specific instance of the class

class User:
    'the static attribute that all objects share'
    user_count = 0

    def __init__(self, username:str, email:str, password:str):
        self.username = username
        self.password = password
        self.__email = email
        User.user_count += 1
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email:str):
        if '@' in new_email:
            self.__email = new_email
    
    


user1 = User('rex', 'rex@gmail.com', '1234')
user2 = User('john', 'john@gmail.com', '1234')
user3 = User('smith', 'smith@gmail.com', '1234')
user4 = User('donald', 'donald@gmail.com', '1234')

print(user1.email)
print(f'Total mumber of users: {User.user_count}')
print(f'Total number of users: {user1.user_count}')



