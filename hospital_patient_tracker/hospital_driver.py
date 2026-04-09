#---------------------------------------
#------K2 CVU/CVICU Unit Simulator------
#---------------------------------------


#Importing the necessary modules
import patient_info, vital_signs

#Global variables 
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

# Getting all he valid rooms in the unit
valid_rooms = {
    "CVICU": {
        "K0263", "K0264", "K0265", "K0266", "K0267", "K0268", "K0269","K0270", 
        "K0272", "K0273", 
        "K0274", "K0275", "K0276", "K0277",
    },

    "CVU": {
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
        print("7. View one patient's information")
        print("8. Update one patient's vital signs")
        print("9. View one patient's vital signs")
        print("10. Exit")
        choice = int(input("Please select your choice: ")) 
        
        if choice >=1 and choice <=10:
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
def admit_patient(cardiology_units, unit_capacities, valid_rooms):

    unit = input("Please enter the unit the patient is going to be admited (CVICU or CVU): ").strip()

    if unit not in cardiology_units:
        print("Invalid unit.")
        return
    if len(cardiology_units[unit]) >= unit_capacities[unit]:
        print(f"{unit} is full. Cannot admit more patients.")
        return

    #Asking for the room the patient is going to be admitted to
    room = input("Please enter the admitting room: ").strip().upper()
    
    if room not in valid_rooms[unit]:
        print(f"{room} is not a valid room in {unit}.")
        return

    for existing_patient in cardiology_units[unit].values():
        if existing_patient.room == room:
            print(f"Room {room} is already occupied.")
            return
    
    #Asking for the MRN of the patient
    mrn = int(input("Please enter the patient's MRN: "))
    
    if mrn in cardiology_units[unit]:
        print("A patient with this MRN already exists in this unit")
        return 
    

    name = input("Please enter the patient's name: ")
    age = int(input("Please enter the patient's age: "))
    gender = input("Please enter the patient's gender: ")
    admission_date = input("Please enter the admitting date: ")
    team_doctor = input("Please enter the team of doctor: ")
    diagnosis = input("Please enter the diagnosis: ")
    isolation = input("Please enter the isolation status: ")
    level_intervention = input("Please enter the level of intervention: ")
    
    past_hx_input = input("Please enter ast medical history (comma separated): ")
    past_hx = [item.strip() for item in past_hx_input.split(",") if item.strip()]
    
    allergies_input = input("Please enter the allergies (comma separated): ") 
    allergies = [item.strip() for item in allergies_input.split(",") if item.strip()]

    type_sx = input("Please enter the type of surgery: ")

    procedures_input = input("Please enter the procedures done (comma separated): ")
    procedures = [item.strip() for item in procedures_input.split(",") if item.strip()]

    rhythm= input("Please enter the cardiac rhythm: ")
    ventilation= input("Please enter the ventilation status: ")

    iv_access_input = input("Please enter the IV accesses (comma separated): ")
    iv_access= [item.strip() for item in iv_access_input.split(",") if item.strip()]

    nutrition_input = input("Please enter the nutrition status (comma separated): ")
    nutrition= [item.strip() for item in nutrition_input.split(",") if item.strip()]

    dressings_input = input("Please enter the dressings present (comma separated): ")
    dressings= [item.strip() for item in dressings_input.split(",") if item.strip()]
    
    elimination= input("Please enter the elimination status: ")
    mobility= input("Please enter the mobility status: ")
    
    #Can fix so that we could input valid labs (Like Na, K, etc)
    labs_input = input("Please enter the critical labs (comma separated): ")
    labs = [item.strip() for item in labs_input.split(",") if item.strip()]

    medications_input = input("Please enter the medication list (comma separated): ")
    medications = [item.strip() for item in medications_input.split(",") if item.strip()]

    issues_input = input("Please enter the current issues (comma separated): ")
    issues= [item.strip() for item in issues_input.split(",") if item.strip()]
    plans= input("Please enter the plan: ")

    pros_involved_input = input("Please enter the pros involved (comma separated): ")
    pros_involved= [item.strip() for item in pros_involved_input.split(",") if item.strip()]
    home_screen= input("Please enter the home situation: ")
    possible_dc= input("Please enter the possible D/C date: ")

    patient = patient_info.Patient(
        unit,
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
    
    cardiology_units[unit][mrn] = patient
    #To test
    patient.display_info()
    print(f"\nPatient {mrn}: {name} successfully admitted to {unit} in room {room}.")
    print("---------------------------------------")

# Discharging a patient from the unit 
def discharge_patient(cardiology_units):

    patient_mrn = int(input("Enter the MRN of the patient you want to discharge: "))

    for unit, patients in cardiology_units.items():  #Key: CVU, Values: Patients technically

        if patient_mrn in patients:
            discharged_patient = patients[patient_mrn]
            del patients[patient_mrn]

            print(f"\nPatient {discharged_patient.mrn} {discharged_patient.name} has been discharged from {unit} successfully.")
            return

    print("\nNo patient found with that MRN.")

# Transferring a patient to another unit or changing rooms in the same unit
def transfer_patient(cardiology_units, unit_capacities, valid_rooms):

    current_unit = input("Enter the current unit (CVICU or CVU): ").strip().upper()

    if current_unit not in cardiology_units:
        print("Invalid current unit.")
        return

    patient_mrn = int(input("Enter the MRN of the patient you want to transfer: "))

    if patient_mrn not in cardiology_units[current_unit]:
        print("No patient found with that MRN in this unit.")
        return

    patient = cardiology_units[current_unit][patient_mrn]

    destination_unit = input("Enter the destination unit (CVICU or CVU): ").strip().upper()

    if destination_unit not in cardiology_units:
        print("Invalid destination unit.")
        return

    new_room = input("Enter the new room: ").strip().upper()

    if new_room not in valid_rooms[destination_unit]:
        print(f"{new_room} is not a valid room in {destination_unit}.")
        return

    if destination_unit == current_unit and new_room == patient.room:
        print("Patient is already in that room.")
        return

    for existing_patient in cardiology_units[destination_unit].values():
        if existing_patient.room == new_room:
            print(f"Room {new_room} is already occupied.")
            return

    # Same unit = just room change
    if destination_unit == current_unit:
        old_room = patient.room
        patient.room = new_room
        print(f"\nPatient {patient.name} has been moved from room {old_room} to room {new_room} in {current_unit}.")
        return

    # Different unit = full transfer
    if len(cardiology_units[destination_unit]) >= unit_capacities[destination_unit]:
        print(f"{destination_unit} is full. Cannot transfer patient.")
        return

    del cardiology_units[current_unit][patient_mrn]

    patient.unit = destination_unit
    patient.room = new_room

    cardiology_units[destination_unit][patient_mrn] = patient

    print(f"\nPatient {patient.name} has been transferred from {current_unit} to {destination_unit} in room {new_room}.")

# Helper Function to manage change the lists
def update_list_field(item_list, field_name):
    
    while True:
        print(f"\nCurrent {field_name}: {item_list}")
        print(f"1. Add to {field_name}")
        print(f"2. Remove from {field_name}")
        print("3. Return")

        choice = input("Select an option: ")

        if choice == "1":
            new_item = input(f"Enter item to add to {field_name}: ")
            if new_item:
                item_list.append(new_item)
                print(f"{new_item} added to {field_name}.")
        
        elif choice == "2":
            remove_item = input(f"Enter item to remove from {field_name}: ").strip()
            if remove_item in item_list:
                item_list.remove(remove_item)
                print(f"{remove_item} removed from {field_name}.")
            else:
                print("Item not found.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")

# Updating a patient's information as needed 
def update_pt_information (cardiology_units):

    current_unit = input("Enter the current unit (CVICU or CVU): ").strip().upper()

    if current_unit not in cardiology_units:
        print("Invalid current unit.")
        return

    patient_mrn = int(input("Enter the MRN of the patient you want to transfer: "))

    if patient_mrn not in cardiology_units[current_unit]:
        print("No patient found with that MRN in this unit.")
        return

    patient = cardiology_units[current_unit][patient_mrn]

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
            update_list_field(patient.past_hx, "Past medical history")
            print("Past medical history updated successfully.")

        elif choice == 7:
            update_list_field(patient.allergies, "Allergies")
            print("Allergies updated successfully.")

        elif choice == 8:
            patient.type_sx = input("Enter the updated type of surgery: ")
            print("Type of surgery updated successfully.")

        elif choice == 9:
            update_list_field(patient.procedures, "Procedures")
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
            update_list_field(patient.nutrition, "Nutrition")
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
            update_list_field(patient.labs, "Labs")
            print("Labs updated successfully.")

        elif choice == 18:
            update_list_field(patient.medications, "Medications")
            print("Medications updated successfully.")

        elif choice == 19:
            update_list_field(patient.issues, "Issues")
            print("Issues updated successfully.")

        elif choice == 20:
            patient.plans = input("Enter the updated plans: ")
            print("Plans updated successfully.")

        elif choice == 21:
            update_list_field(patient.pros_involved, "Professionals Involved")
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

def update_vital_signs(patients):

    mrn = int(input("Enter the patient's MRN: "))

    if mrn not in patients:
        print("Patient not found.")
        return

    systolic_bp = int(input("Enter systolic BP: "))
    diastolic_bp = int(input("Enter diastolic BP: "))
    heart_rate = int(input("Enter heart rate: "))
    respiratory_rate = int(input("Enter respiratory rate: "))
    oxygen_saturation = int(input("Enter oxygen saturation: "))
    temperature = float(input("Enter temperature: "))

    latest_vitals = vital_signs.VitalSigns(
        systolic_bp,
        diastolic_bp,
        heart_rate,
        respiratory_rate,
        oxygen_saturation,
        temperature
    )

    patients[mrn].vital_signs = latest_vitals
    print("Vital signs updated successfully.")  

def view_latest_vital_signs(patients):
    
    mrn = int(input("Enter the patient's MRN: "))

    if mrn not in patients:
        print("Patient not found.")
        return

    patient = patients[mrn]

    if patient.vital_signs is None:
        print("No vital signs recorded yet.")
        return

    print(f"\nLatest vital signs for {patient.room} {patient.name} {patient.mrn}:")
    patient.vital_signs.display_vitals()


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
                admit_patient(cardiology_units, unit_capacities, valid_rooms)
                print("*" * 40)

            # Discharging patient from unit
            case 2:
                print("Discharging a patient")
                discharge_patient(cardiology_units)
                print(cardiology_units)
                print("*" * 40)
            
            # Transferring a patient to another unit
            case 3:
                print("Transferring a patient to another unit")
                transfer_patient(cardiology_units, unit_capacities, valid_rooms)
                print(cardiology_units)
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
                print("Update one patient's vital_signs")
                update_vital_signs(patients)
                print("*" * 40)
            case 9:
                print("View one patient's vital_signs")
                view_latest_vital_signs(patients)
                print("*" * 40)

            case 10:
                print("Exiting")
                break
            case _:
                print("Invalid choice. Try again!")

    
    print("Thank you for visiting the unit! Application now closing")
    

    