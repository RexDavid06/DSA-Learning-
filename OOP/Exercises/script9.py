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