from flask import json

import json, expence

FILE = 'users.json'


user = {"name": "", "email": "", "password": ""}

def register():
    print("====== REGISTER FORM======")
    

    user['name'] = input("Enter your full name:").capitalize()
    user['email'] = input("Enter your email: ").lower()
    user['password'] = input("Enter your password: ")
    c_password = input("Confirm password: ")
    

    if user["email"].endswith("@gmail.com") == False:
        print("Your email Invalid ")
    elif user['password'] != c_password:
        print("Password are not match") 
    else:
        
        try:
            with open(FILE, 'r')as file:
                users = json.load(file)

        except :
            users = []
        users.append(user)  
        with open(FILE, 'w') as file:
            json.dump(users, file, indent = 4)
        print("\n ======== Registeration successfull=======\n")
            
            

    
def login():

    with open(FILE, 'r')as f:
        users = json.load(f)

    print("====== LOGIN FORM =======\n")
    if len(users) == 0:
        print(f"users are not found")
    
    elif len(users) > 0:

        email = input("Enter your email: ").lower()
        password = input("Enter your passowrd: ")
        
        for i in range(len(users)):
            for j in range(len(users)):
    
                if email == users[i]['email'] and password == users[i]['password']:
                    
                    print("\n ======Login successfull=======\n")
                    expence.exp()
                    break

                elif email != users[i]['email'] or password != users[i]['password']:
                    print("\n ---->> User are not found \n ")
                    print("plz register ") 

                    break
            
    else:

        print("INVALID CREDITIALS ")
