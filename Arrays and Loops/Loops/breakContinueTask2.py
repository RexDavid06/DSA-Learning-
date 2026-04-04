# scan through a  list of  emails to block unsafe  data from entering your system


emails = [
    'data@gmail.com',
    'bara@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com,'
]

for email in emails:
    if ';' in email:
        print('SQL Injection Attack Detected')
        break
    print(f"Processing Email: {email}")