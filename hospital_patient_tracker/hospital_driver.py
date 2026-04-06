#---------------------------------------
#------K2 CVU/CVICU Unit Simulator------
#---------------------------------------


#Importing the necessary modules

def welcome():
        print('+++++++++++++++++++++++++++++++++++++++++++')
        print('Welcome to the K2 CVU/CVICU Unit Simulator!')
        print('+++++++++++++++++++++++++++++++++++++++++++')

def menu():
          
        print("Select what you would like to do")
        print("1. Add a patient to the unit")
        print("2. Discharge patient from the unit")
        print("3. Update patient")
        print("4. View all patients")
        print("5. View one patient")
        print("6. Exit")
        choice = int(input("Please select your choice: ")) 
        return choice 

class Hospital_Driver:
    

    # Display welcome banner
    welcome()

    while True:
           
           #Showing the menu and getting the input
           menu_choice = menu()

           

    

    

    