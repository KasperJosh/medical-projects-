#---------------------------------------
#------K2 CVU/CVICU Unit Simulator------
#---------------------------------------


#Importing the necessary modules
import patient_info

def welcome():
        print('+++++++++++++++++++++++++++++++++++++++++++')
        print('Welcome to the K2 CVU/CVICU Unit Simulator!')
        print('+++++++++++++++++++++++++++++++++++++++++++')

def menu():
          
        
        print("Select what you would like to do")
        print("1. Admit a patient to the unit")
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
              
# Adding a patient to the unit method
def admit_patient(patients):
        
    room = input("Please enter the admitting room: ")
    name = input("Please enter the patient's name: ")
    mrn = int(input("Please enter the patient's MRN: "))
    age = int(input("Please enter the patient's age: "))
    gender = input("Please enter the patient's gender: ")
    admission_date = input("Please enter the admitting date: ")
    team_doctor = input("Please enter the team of doctor: ")
    diagnosis = input("Please enter the diagnosis: ")
    isolation = input("Please enter the isolation status ")
    level_intervention = input("Please enter the level of intervention ")
    past_hx = input("Please enter the past medical history ")
    allergies = input("Please enter the allergies: ")
    type_sx = input("Please enter the type of surgery: ")
    procedures =input("Please enter the procedures done: ")
    rhythm= input("Please enter the cardiac rhythm: ")
    ventilation= input("Please enter the ventilation status: ")
    iv_access= input("Please enter the IV accesses: ")
    nutrition= input("Please enter the nutrition status: ")
    dressings= input("Please enter the dressings present: ")
    elimination= input("Please enter the elimination status ")
    mobility= input("Please enter the mobility status: ")
    labs = input("Please enter the critical labs")
    medications = input("Please enter the medication list ")
    issues= input("Please enter the current issues: ")
    plans= input("Please enter the plan: ")
    pros_involved= input("Please enter the pros involved: ")
    home_screen= input("Please enter the home situation: ")
    possible_dc= input("Please enter the p0ssible D/C date ")

    patient = patient_info.Patient(
        room,
        name,
        mrn,
        age,
        gender,
        admission_date,
        team_doctor,
        diagnosis,
        isolation ,
        level_intervention,
        past_hx,
        allergies,
        type_sx,
        procedures,
        rhythm,
        ventilation,
        iv_access,
        nutrition,
        dressings,
        elimination,
        mobility,
        labs,
        medications,
        issues,
        plans,
        pros_involved,
        home_screen,
        possible_dc
    )
    
    patients[mrn] = patient
    #To test
    patient.display_info()
    print("Patient successfully added!")


class Hospital_Driver:
    
    #Creating a dictionary that will store all the patients
    # key = MRN , value = Patient Object
    patients ={}

    # Display welcome banner
    welcome()

    while True:
           
        #Showing the menu and getting the input
        menu_choice = menu()

        match menu_choice:

            # Adding a patient to the unit
            case 1:  
                print("Admit a patient")
                admit_patient(patients)
                print(patients)
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
    

    