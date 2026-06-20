# Abstraction
# the aim of Abstraction is to reduce complexity by hiding unecessary details. (It allows users to focus on what an object does rather than how it does it)

'''
In this class, we assume we have multiole methods but the user needs to focus on just one without the other complexity'''

class EmailService:
    def _connect(self):
        print('connecting to the email service server....')
    
    def _authenticate(self):
        print('Authenticating the connected user...')

    def send_email(self):
        self._connect()
        self._authenticate()
        print('sending email....')
        print('Email Sent')
        self._disconnect()
    
    def _disconnect(self):
        print('Disconnecting from server')


mail = EmailService()
mail.send_email()