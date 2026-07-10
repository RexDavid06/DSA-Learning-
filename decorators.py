def func(f):
    def wrapper():
        print('wrapper started')
        f()
        print('wrapper stopped')
    return wrapper()


@func
def func1():
    print(f"Life's long dream")


def login(f):
    def wrapper():
        db_user = 'Rex'
        db_password = 'rex123'
        username = str(input('Input your username: '))
        password = input('Input your password: ')
        if username == db_user and password == db_password:
            f()
            print(f'{username}: Your are welcome')
        
        else:
            print(f'You are not known')
    return wrapper()
    
@login
def view_profile():
    print('Your page is still in progress....')


