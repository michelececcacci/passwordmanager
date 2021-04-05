import json
import sys

def main():
    while True:
        first_input = input('''welcome to passwordmanager v0.0.0, press 1 if you are already registered, 
        2 if you want to register and 3 if you want to quit >''')
        template = {"users" : {}}
        if first_input == '1':
            print('Looks like you want to log-in >')
            try: 
                with open('data.json', 'r') as f:
                    pass
            except:
                with open('data.json', 'w') as f:
                    json.dump(template, f, indent = 4)
            #1st input lets user login, then tests if login is correct and lets user access his passwords.
            inputdata = username_and_password()
            for person in f['users']:
                if person["username"] == inputdata[0] and person["username"] == inputdata[1]:
                    print("Login successful")
                    manage_passwords(inputdata[0])
            sys.exit()
                    
        elif first_input == '2':
            print("Looks like you want to register")
            try:
                with open('data.json', 'a') as f:
                    pass
            except:
                with open('data.json', 'w') as f:
                    json.dump(template, f) 
            inputdata = username_and_password()
            for person in f['users']:
                if person['username'] == inputdata[0]:
                    print(f"username {inputdata[0]} already used")
                    sys.exit()

                #otherwise let user register  password and username
        elif first_input == '3': #just exit if user wants to quit program.
            sys.exit()

def username_and_password():
    username = input('please input your username >')
    password = input('please input your password >') 
    return [username, password]

def manage_passwords(user):
    pass
main()