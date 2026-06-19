'''Exercise 9 (Challenge): User Registration

Create a User class.

Requirements:

Instance attributes:

username
email
password

Static methods:

is_valid_email(email)
is_strong_password(password)

Rules:

Email:

Must contain "@"
Must contain "."

Password:

At least 8 characters
At least one digit
At least one uppercase letter

Example:

print(User.is_valid_email("rex@gmail.com"))
print(User.is_strong_password("Python123"))

Expected understanding:

Real-world validation using static methods.'''

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def is_valid_email(email):
        if '@' in email and '.' in email:
            return f'{email} is a valid email!'
        else:
            return f"{email} isn't a valid email, and can't be used!"

    @staticmethod
    def is_strong_password(password):
        if len(password) >= 8:
            for char in password:
                if char.isdigit():
                    for char in password:
                        if char.isupper():
                            return f'{password} is a strong password!'
        return f"{password} isn't a strong password, and can't be used!"
                        
    
            



user1 = User('rex', 'rex@gmail.com', '3456yhbesfg')
print(User.is_valid_email(user1.email))
print(User.is_strong_password(user1.password))