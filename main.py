import json
import sys

def main():
    while True:
        first_input = input('''welcome to passwordmanager v0.0.0, press 1 if you are already registered, 
        2 if you want to register and 3 if you want to quit >''')
        if first_input == '1':
            new_file = {"users" :{}}
            print('Looks like you want to log-in >')
            userdata = username_and_password()
            try:
                with open('passwords.json', 'r') as f:
                    pass
            except:
                with open('passwords.json', 'w') as f:
                    json.dump(new_file, f)
            #1st input lets user login, then tests if login is correct and lets user access his passwords.
        elif first_input == '2':
            username_and_password()
            try:
                open('passwords.json', 'r')
            except:
                open('passwords.json', 'w')
                new_file = {"users" :{}}
            #lets user input his password and username
        elif first_input == '3': #just exit if user wants to quit program.
            sys.exit()
def username_and_password():
    username = input('please input your username >')
    password = input('please input your password >') 
    return [username, password]
main()