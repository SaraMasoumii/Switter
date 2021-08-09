from typing import Text
from database import *
from application import *

a = Application()
print('Welcome to Switter\n')
print('Choose a command:\n Enter 1 for login\n Enter 2 for register')
cm = int(input())

if cm == 1:
    while True:
        username = input('Username:')
        password = input('password:')
        try:
            a.login(username, password)
            break

        except:
            print('Please try again')

else:
    while True:
        username = input('Enter your username:')
        password = input('Enter your password:')
        check_password = input('ReEnter your password:')
        if password != check_password:
            print("passwords don't match!\nPlease try again")

        else:
            try:
                a.register(username, password)
                break

            except:
                print('Please try again')
