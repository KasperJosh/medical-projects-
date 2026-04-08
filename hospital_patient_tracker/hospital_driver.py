#---------------------------------------
#------K2 CVU/CVICU Unit Simulator------
#---------------------------------------


#Importing the necessary modules
import patient_info

# Creating a dictionary to store the patients in each unit
cardiology_units = {
    "CVICU": {}, 
    "CVU": {}
    }

# Setting the unit capacity in both CVICU and CVU 
unit_capacities = {
    "CVICU": 14, 
    "CVU": 37
    }

valid_rooms = {
    "CVICU": {
        "K0263", "K0264", "K0265", "K0266", "K0267", "K0268", "K0269","K0270", 
        "K0272", "K0273", 
        "K0274", "K0275", "K0276", "K0277",
    },

    "Cardiac Step Down": {
        "K0210", "K0211", "K0212",
        "K0214", "K0215", "K0216", "K0217",
        "K0220", "K0221", "K0222", "K0223", "K0224", "K0225", "K0226",
        "K0230", "K0231", "K0232", "K0233", "K0234", "K0235", "K0236",
        "K0240", "K0241", "K0242", "K0243", "K0244", "K0245", "K0246",
        "K0250", "K0251", "K0252", "K0253", "K0254", "K0255", "K0256", "K0257",
        "K0271"
    }
}

#Welcome Banner to the Hospital 
def welcome():
        print('+++++++++++++++++++++++++++++++++++++++++++')
        print('Welcome to the K2 CVU/CVICU Unit Simulator!')
        print('+++++++++++++++++++++++++++++++++++++++++++')

# Main Menu of the Hospital Program
def menu():
          
        print("Select what you would like to do")
        print("1. Admit a patient to the unit")
        print("2. Discharge patient from the unit")
        print("3. Transfer patient to another unit")
        print("4. Update patient information")
        print("5. View all patients")
        print("6. View all patients with their information")
        print("7. View one patient")
        print("8. Exit")
        choice = int(input("Please select your choice: ")) 
        
        if choice >=1 and choice <=8:
            return choice
        else:
            print("Please try again")

# Creating the sub menu to update patient information
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
    
    if 1<= choice <=24:
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
    past_hx = [item.strip() for item in input("Please enter the Past Medical History (comma separated): ").split(",")]
    allergies = [item.strip() for item in input("Please enter the allergies: ").split(",")]
    type_sx = input("Please enter the type of surgery: ")
    procedures = [item.strip() for item in input("Please enter the procedures done: ")]
    rhythm= input("Please enter the cardiac rhythm: ")
    ventilation= input("Please enter the ventilation status: ")
    iv_access= [item.strip() for item in input("Please enter the IV accesses: ").split(",")]
    nutrition= [item.strip() for item in input("Please enter the nutrition status: ").split(",")]
    dressings= [item.strip() for item in input("Please enter the dressings present: ").split(",")]
    elimination= input("Please enter the elimination status: ")
    mobility= input("Please enter the mobility status: ")
    labs = [item.strip() for item in input("Please enter the critical labs: ").split(",")]
    medications = [item.strip() for item in input("Please enter the medication list: ").split(",")]
    issues= [item.strip() for item in input("Please enter the current issues: ").split(",")]
    plans= input("Please enter the plan: ")
    pros_involved= [item.strip() for item in input("Please enter the pros involved: ").split(",")]
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

    mrn = int(input("Enter the MRN of the patient to update: "))

    if mrn not in patients:
        print("Patient not found.")
        return

    patient = patients[mrn]

    #Some of the fields, it's better to put it as a list
    while True:

        choice = pt_update_menu()
        
        if choice == 1:
            patient.room = input("Enter the new room: ")
            print("Room updated successfully.")

        elif choice == 2:
            patient.team_doctor = input("Enter the new doctor/team: ")
            print("Doctor updated successfully.")

        elif choice == 3:
            patient.diagnosis = input("Enter the new diagnosis: ")
            print("Diagnosis updated successfully.")

        elif choice == 4:
            patient.isolation = input("Enter the new isolation status: ")
            print("Isolation status updated successfully.")

        elif choice == 5:
            patient.level_intervention = input("Enter the new level of intervention: ")
            print("Level of intervention updated successfully.")

        elif choice == 6:
            patient.past_hx = input("Enter the updated past medical history: ")
            print("Past medical history updated successfully.")

        elif choice == 7:
            patient.allergies = input("Enter the updated allergies: ")
            print("Allergies updated successfully.")

        elif choice == 8:
            patient.type_sx = input("Enter the updated type of surgery: ")
            print("Type of surgery updated successfully.")

        elif choice == 9:
            patient.procedures = input("Enter the updated procedures: ")
            print("Procedures updated successfully.")

        elif choice == 10:
            patient.rhythm = input("Enter the updated rhythm: ")
            print("Rhythm updated successfully.")

        elif choice == 11:
            patient.ventilation = input("Enter the updated ventilation status: ")
            print("Ventilation updated successfully.")

        elif choice == 12:
            patient.iv_access = input("Enter the updated IV accesses: ")
            print("IV accesses updated successfully.")

        elif choice == 13:
            patient.nutrition = input("Enter the updated nutrition status: ")
            print("Nutrition updated successfully.")

        elif choice == 14:
            patient.dressings = input("Enter the updated dressings: ")
            print("Dressings updated successfully.")

        elif choice == 15:
            patient.elimination = input("Enter the updated elimination status: ")
            print("Elimination updated successfully.")

        elif choice == 16:
            patient.mobility = input("Enter the updated mobility status: ")
            print("Mobility updated successfully.")

        elif choice == 17:
            patient.labs = input("Enter the updated labs: ")
            print("Labs updated successfully.")

        elif choice == 18:
            patient.medications = input("Enter the updated medications: ")
            print("Medications updated successfully.")

        elif choice == 19:
            patient.issues = input("Enter the updated issues: ")
            print("Issues updated successfully.")

        elif choice == 20:
            patient.plans = input("Enter the updated plans: ")
            print("Plans updated successfully.")

        elif choice == 21:
            patient.pros_involved = input("Enter the updated interdisciplinary team involved: ")
            print("Interdisciplinary team updated successfully.")

        elif choice == 22:
            patient.home_screen = input("Enter the updated home situation: ")
            print("Home situation updated successfully.")

        elif choice == 23:
            patient.possible_dc = input("Enter the updated possible discharge date: ")
            print("Possible discharge date updated successfully.")

        elif choice == 24:
            print("Returning to main menu.")
            break

# Viewing all the patient's on the unit
def view_all_patients (patients):
    
    if not patients:
        print("\nThere are no patients currently on the unit.")
        return
    print("\n--All Patients on the Unit--")
    for patient in patients.values():
        print(f"Room: {patient.room} | Name: {patient.name} | MRN: {patient.mrn} | Diagnosis: {patient.diagnosis}")
    print("-" * 40)

# Viewing all the patient's added to the unit so far with their information 
def view_all_patients_with_info(patients):
    
    if not patients:
        print("\nThere are no patients currently on the unit.")
        return
    print("\n--All Patients on the Unit with Information--")
    for patient in patients.values():
        patient.display_info()
        print("-" * 40)

# Viewing all of the information of one patient
def view_one_patient_info(patients):
    
    if not patients:
        print("\nThere are no patients currently on the unit.")
        return
    mrn = int(input("Enter the MRN of the patient to update: "))

    if mrn not in patients:
        print("Patient not found.")
        return

    patient = patients[mrn]
    patient.display_info()

# Main Driver Class
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
                print("*" * 40)

            # Discharging patient from unit
            case 2:
                print("Discharging a patient")
                discharge_patient(patients)
                print(patients)
                print("*" * 40)
            
            # Transferring a patient to another unit
            case 3:
                print("Transferring a patient to another unit")
                transfer_patient(patients)
                print(patients)
                print("*" * 40)

            case 4:
                print("Updating patient information")
                update_pt_information(patients)
                print(patients)
                print("*" * 40)

            case 5:
                print("Viewing all the patients")
                view_all_patients(patients)
                print("*" * 40)

            case 6:
                print("Viewing all the patients with information")
                view_all_patients_with_info(patients)
                print("*" * 40)

            case 7:
                print("Viewing one patient")
                view_one_patient_info(patients)
                print("*" * 40)

            case 8:
                print("Exiting")
                break
            case _:
                print("Invalid choice. Try again!")

    
    print("Thank you for visiting the unit! Application now closing")
    

    