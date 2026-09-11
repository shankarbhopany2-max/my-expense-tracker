import json, auth

from matplotlib.pylab import append

expence =  {"title": "", "amount": 0.0, "category": "", "date": ""}


FILE="data.json"

def exp():
    while True:
        print("""==========================
        EXPENCE TRACKER
    ==========================""")
        print("1. Add Expence")
        print("2. view Expence")
        print("3. Update Expence")
        print("4. Delete Expence")
        print("5. Search Expence")
        print("6. Total Expence")
        print("7. Category Expence")
        print("8. Monthly Expence")
        print("9. Export Expence")
        print("10. Logout")
        print("11. Exit")
# user input choice 
        choice = input ("Enter your choice : ")
# condition 1
        if choice == '1':
            expence['title'] = input ("Enter the Title: ")
            expence['amount'] =float(input("Enter the amount: "))
            expence['category'] = input("category: ")
            expence['date'] = input("Enter the date (YYYY-MM-DD): ")
            try:
                with open(FILE, 'r')as file:
                    datas = json.load(file)
                    

            except:
                datas =[] 
            datas.append(expence)
            with open(FILE, 'w')as file:
                json.dump(datas, file, indent = 4)
                
            

     
        elif choice == '2':
            print("\n your ALL Expences here")
            with open(FILE, 'r')as f:
                data = json.load(f)
            if len(data) == 0:
                print("expences file empty")
            else:
                for i in range(len(data)):
                    print(f"{data.index(data[i])}. {data[i]}")

           
                    
            
        elif choice == '3':
            with open(FILE, "r") as file:
                data = json.load(file)
            print(len(data))
            if len(data) == 0:
                print("expences file empty")
            else:

                for i in range (len(data)):
                    print(f"{data.index(data[i])}. {data[i]}")

            # print(type(data))
                num = int(input("Enter expence number: \n"))
                
                expence["title"] = input("Enter the Title")
                expence['amount'] =float(input("Enter the amount: "))
                expence['category'] = input("category: ")
                expence['date'] = input("Enter the date (YYYY-MM-DD): ")

                data[num] = expence
            
                with open (FILE, 'w')as f:
                    json.dump(data, f, indent = 4)


            
        elif choice == '4':
            with open(FILE, 'r')as f:
                b = json.load(f)

            if len(b) == 0:
                print("Expences DB file empty")
            else:
                print("ALL EXPENCES ARE HERE ")
                for i in range(len(b)):

                    print(f"{b.index(b[i])}. {b[i]}")

                num = int(input("Enter expence number you want to delete: "))
                for i in range(len(b)):
                    b.remove(b[num])
                
                
        
                

        elif choice == '5':
            with open(FILE, 'r')as f:
                db = json.load(f)

            if len(db) == 0:
                print("Expences DB file empty")
            search = input(str("search any catagory,  title, or price: "))

            for i in range(len(db)):
                for j in db[i]:
                    if search == db[i][j]:
                        print(f"{i} . {db[i]}")
                    
                    


        elif choice == '6':
            print("Total ")
            with open(FILE, 'r')as f:
                db = json.load(f)
            
            if len(db) == 0:
                print("Expences DB file empty")
            print(f"Total expences : {len(db)}" )

            

        elif choice == '7':
    
            with open(FILE, 'r')as file:
                db = json.load(file)
                # print(db)
            print("Total expence categories: ")
            for i in range(len(db)):
                print(f" {db[i]['Category']}")


            

        elif choice == '8':
            print("monthly")

        elif choice == '9':
            print("Export data in csv file")
            with open(FILE, 'r')as file:
                db = json.load(file)

            FILES = 'reports.csv'
            d = []
            for i in range(len(db)):
                with open(FILES, 'w')as file:
                    json.dump(d, file)
                d.append(db[i])
                    
                
            
            


        elif choice == '10':
            print("== User Logout successfully ==")
                            
            print("A. login ")
            print("B. register")
            choice = input("Enter your (A/B): ")
            if choice == "A" or "a":
                auth.login()
            elif choice == "B" or "b":
                auth.register()
            else:
                print ("invalid choice")
        
                    
                
        elif choice == '11':
            print("program Exit")
            break
            

        else:
            print("Invalid credintionals")
            break





