# main.py
import json
import auth
import expence

while True:
    print("===================================WELCOME EXPENCE TRACKER=================================")
    print('''
   -----> if your new register and login than excces our services thankyou 
''')
    
    print("A. Register")
    print("B. Login")
    print("C. Exit")

    choice = input("SELECT IN THIS OPTION (A/B): ") 

    FILE = "users.json"

    if choice == "A" or choice == "a":
        auth.register()
        

    
                    
    elif choice == "B" or choice == "b":
        auth.login()
        
    elif choice == "C" or choice == "c":
        print("Program Exit successfully")
        break

    else: 
        print("Invalid choice")
