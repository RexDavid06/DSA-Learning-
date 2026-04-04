# Simulate a LOGIN SYSTEM
#User has 3 attempts

correct_password = "1234"

for attempt in range(3):
    password = input('Input the password: ')

    if password == correct_password:
        print('Access Granted')
        break
    else:
        print('Wrong Password')
else:
    print('Access Denied')

