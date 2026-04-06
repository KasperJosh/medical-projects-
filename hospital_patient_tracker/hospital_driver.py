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
        print("3. Transfer patient to another unit")
        print("4. Update patient information")
        print("5. View all patients")
        print("6. View one patient")
        print("7. Exit")
        choice = int(input("Please select your choice: ")) 
        
        if choice >=1 and choice <=7:
            return choice
        else:
            print("Please try again")
              

class Hospital_Driver:
    

    # Display welcome banner
    welcome()

    while True:
           
        #Showing the menu and getting the input
        menu_choice = menu()

        match menu_choice:

            # Adding a patient to the unit
            case 1:  
                print("Adding a patient")
                break
            # Discharging patient from unit
            case 2:
                print("Discharging a patient")
                break
            # Transferring a patient to another unit
            case 3:
                print("Transferring a patient to another unit")
                break
            case 4:
                print("Updating patient information")
                break
            case 5:
                print("Viewing all the patients")
                break
            case 6:
                print("Viewing one patient")
                break
            case 7:
                print("Exiting")
                break
            case _:
                print("Invalid choice. Try again!")

        while(menu_choice !=7):
            print("Thank you for visiting the unit! Application now closing")
    

    