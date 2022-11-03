import sys

from database import Database as db

sys.path.append('./database')

def create_employee():    

    while True:
        print("[1] Generate new employee")
        print("[2] Back")

        selection = 0

        try:
            selection = int(input(""))
        except:
            print("Invalid selection. Try again.")
        
        if selection == 1:
            while True:
                print("\nPress enter to generate new employee, type anything else to cancel.")        
                key = input("")
                
                if key == "":
                    new_employee = db().generate_employee()
                    db().insert(new_employee)                                        
                else:
                    break     
                    #employee_details = db().select(unique_id=new_employee['unique_id'])
        elif selection == 2:
            break

def search():
    employees = db().select_all()

    while True:
        print("[1] Search by name")
        print("[2] Search by skills")
        print("[3] Search managers")
        print("[4] Back")

        selection = 0
        
        try:
            selection = int(input(""))    
        except:
            print("\nError occured. Try again.\n")
            continue

        if selection == 1:
            print("Please enter name: ")
            name = input("")
            
            found = False    
            count = 1        
            for key, val in employees.items():
                if name.lower() == employees[key]['name'].lower():                    
                    print(count, employees[key])                    
                    found = True                    
                    count += 1
            print("\n")
            if found == False:
                print("Could not find employee with name: '{}'".format(name))
        
        elif selection == 2:
            print("Please enter skill: ")
            skill = input("")
            found = False
            count = 1                        
            for key, val in employees.items():
                if skill.lower() in employees[key]['skills'].lower():                    
                    print(count, employees[key])                     
                    found = True
                    count += 1
            print("\n")
            if found == False:
                print("Could not find employee with skill: '{}'".format(skill))
                    
        
        elif selection == 3:
            found = False
            count = 1
            for key, val in employees.items():
                if employees[key]['manager'] == 'Yes':                    
                    print(count, employees[key])                
                    found = True
                    count += 1
            print("\n")
            if found == False:
                print("Currently, no managers exist.")
        
        elif selection == 4:
            break

if __name__ == "__main__":
    # create database
    db().create()
    
    while True:
        print("Welcome to the database!")
        print("[1] Search for Employee")
        print("[2] Create Employee") 
        print("[3] Exit")

        selection = 0
        
        try:
            selection = int(input(""))            
        except:
            print("Error")
            
        if selection == 1:
            search()
        elif selection == 2:
            create_employee()
        elif selection == 3:
            break

"""create a "press enter to create random employee entry" """
