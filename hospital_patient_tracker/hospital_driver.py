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


def pt_update_menu():
    
    print("Select what you would like to do")
    print("1. Update patient's room")
    print("2. Update patient's doctor")
    print("3. Update diagnosis")
    print("4. Update isolation status")
    print("5. Update level of intervention")
    print("6. Update past medical history")
    print("7. Update allergies")
    print("8. Update the type of surgery")
    print("9. Update the procedures")
    print("10. Update the rhythm")
    print("11. Update the ventilation status")
    print("12. Update the IV accesses")
    print("13. Update the nutrition status")
    print("14. Update the dressings")
    print("15. Update the elimination status")
    print("16. Update the mobility status")
    print("17. Update the labs")
    print("18. Update the medications")
    print("19. Update the issues")
    print("20. Update the plans")
    print("21. Update the interdisciplinary team involved")
    print("22. Update the home situation")
    print("23. Update the possible discharge date")
    print("24. Exit")
    choice = int(input("Please select your choice: ")) 
    
    if choice >=1 and choice <=24:
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
    isolation = input("Please enter the isolation status: ")
    level_intervention = input("Please enter the level of intervention: ")
    past_hx = input("Please enter the Past Medical History: ")
    allergies = input("Please enter the allergies: ")
    type_sx = input("Please enter the type of surgery: ")
    procedures =input("Please enter the procedures done: ")
    rhythm= input("Please enter the cardiac rhythm: ")
    ventilation= input("Please enter the ventilation status: ")
    iv_access= input("Please enter the IV accesses: ")
    nutrition= input("Please enter the nutrition status: ")
    dressings= input("Please enter the dressings present: ")
    elimination= input("Please enter the elimination status: ")
    mobility= input("Please enter the mobility status: ")
    labs = input("Please enter the critical labs: ")
    medications = input("Please enter the medication list: ")
    issues= input("Please enter the current issues: ")
    plans= input("Please enter the plan: ")
    pros_involved= input("Please enter the pros involved: ")
    home_screen= input("Please enter the home situation: ")
    possible_dc= input("Please enter the possible D/C date: ")

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
    print(patients)
    print("---------------------------------------")


# Discharging a patient from the unit 
def discharge_patient(patients):

    patient_mrn = int(input("Enter the MRN of the patient you want to discharge: "))

    if patient_mrn in patients:
        discharged_patient = patients [patient_mrn]
        del patients[patient_mrn]
        print(f"\nPatient {discharged_patient.name} has been discharged successfully.")
    
    else:
        print("\nNo patient found with that MRN.")

# Transferring a patient to another unit

def transfer_patient(patients):

    patient_mrn = int(input("Enter the MRN of the patient you want to transfer: "))
    if patient_mrn in patients:
        transferred_patient = patients [patient_mrn]
        
        transfer_location = input("Enter the location where you want to transfer the patient: ")
        
        del patients[patient_mrn] #To fix
        print(f"\nPatient {transferred_patient.name} has been transferred successfully to {transfer_location}.")
    
    else:
        print("\nNo patient found with that MRN.")

# Updating a patient's information as needed 
def update_pt_information (patients):

    mrn = input("Enter the MRN of the patient to update: ")

    if mrn not in patients:
        print("Patient not found.")
        return

    patient = patients[mrn]


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
                
                

            # Discharging patient from unit
            case 2:
                print("Discharging a patient")
                discharge_patient(patients)
                print(patients)
                

            # Transferring a patient to another unit
            case 3:
                print("Transferring a patient to another unit")
                
            case 4:
                print("Updating patient information")
                
            case 5:
                print("Viewing all the patients")
                
            case 6:
                print("Viewing one patient")
                
            case 7:
                print("Exiting")
                break
            case _:
                print("Invalid choice. Try again!")

    
    print("Thank you for visiting the unit! Application now closing")
    

    