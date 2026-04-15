#---------------------------------------
#------K2 CVU/CVICU Unit Simulator------
#---------------------------------------


#Importing the necessary modules
import patient_info, vital_signs
from input_helpers import (
    get_nonempty_input,
    get_int_input,
    get_list_input,
    get_valid_standard_single,
    get_valid_standard_multi
)

from patient_acuity_score import get_patient_assignment_score
# scores = get_patient_assignment_score(patient)
#print(scores)

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
    print("8. Update one patient's Vital Signs")
    print("9. View one patient's Vital Signs")
    print("10. View CVU/CVICU Bedflow Status")
    print("11. View patients ranked by acuity")
    print("12. View patients ranked by total weighted score")
    print("13. Exit")

    try:
        choice = int(input("Please select your choice: "))
        if 1 <= choice <= 13:
            return choice
        else:
            print("Please try again")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

# Creating the sub menu to update patient information
def pt_update_menu():
    
    print("\n--- UPDATE PATIENT INFORMATION ---")
    print("Select what you would like to update:")

    print("1. Update team doctor")
    print("2. Update diagnosis")
    print("3. Update isolation status")
    print("4. Update level of intervention")
    print("5. Update past medical history")
    print("6. Update allergies")
    print("7. Update type of surgery")
    print("8. Update procedures/tests")

    print("9. Update hemodynamic status")
    print("10. Update cardiac status")
    print("11. Update respiratory status")
    print("12. Update neurological status")
    print("13. Update lab instability")
    print("14. Update safety risk")
    print("15. Update behaviour/cooperation")
    print("16. Update medication complexity")
    print("17. Update CBGM frequency")
    print("18. Update monitoring frequency")

    print("19. Update IV access")
    print("20. Update nutrition")
    print("21. Update wounds/dressings")
    print("22. Update elimination")
    print("23. Update mobility")
    print("24. Update pain management")
    print("25. Update communication")
    print("26. Update family/social")
    print("27. Update blood test frequency")

    print("28. Update medications")
    print("29. Update issues")
    print("30. Update plans")
    print("31. Update professionals involved")
    print("32. Update home situation")
    print("33. Update turnover")
    print("34. Update special flags")

    print("35. Exit")

    try:
        choice = int(input("Please select your choice: "))
        if 1 <= choice <= 35:
            return choice
        else:
            print("Invalid choice. Please try again.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None
              
# Adding a patient to the unit method
def admit_patient(cardiology_units, unit_capacities, valid_rooms):

    unit = input("Please enter the unit the patient is going to be admitted (CVICU or CVU): ").strip().upper()

    if unit not in cardiology_units:
        print("Invalid unit.")
        return

    if len(cardiology_units[unit]) >= unit_capacities[unit]:
        print(f"{unit} is full. Cannot admit more patients.")
        return

    #Asking the admitting room
    room = input("Please enter the admitting room: ").strip().upper()

    if room not in valid_rooms[unit]:
        print(f"{room} is not a valid room in {unit}.")
        return

    for existing_patient in cardiology_units[unit].values():
        if existing_patient.room == room:
            print(f"Room {room} is already occupied.")
            return

    #Asking the user for the MRN
    mrn = get_int_input("Please enter the patient's MRN: ")

    if mrn in cardiology_units[unit]:
        print("A patient with this MRN already exists in this unit.")
        return

    name = get_nonempty_input("Please enter the patient's name: ")
    age = get_int_input("Please enter the patient's age: ")
    gender = get_nonempty_input("Please enter the patient's gender: ").strip().upper()
    admission_date = get_nonempty_input("Please enter the admitting date: ")
    team_doctor = get_nonempty_input("Please enter the team doctor: ")
    diagnosis = get_valid_standard_single(
        "diagnosis",
        "Please enter the diagnosis: "
    )

    isolation_status = get_valid_standard_single(
        "isolation_status",
        "Please enter the isolation status: "
    )

    level_of_intervention = get_valid_standard_single(
        "level_of_intervention",
        "Please enter the level of intervention: "
    )

    pmhx = get_valid_standard_multi(
        "pmhx",
        "Please enter past medical history (comma separated): "
    )

    allergies = get_list_input(
        "Please enter the allergies (comma separated): "
    )

    type_sx = get_nonempty_input("Please enter the type of surgery (or N/A): ").strip().upper()

    procedures_tests = get_valid_standard_multi(
        "procedures_tests",
        "Please enter the procedures/tests (comma separated): "
    )

    hemodynamic_status = get_valid_standard_single(
        "hemodynamic_status",
        "Please enter the hemodynamic status: "
    )

    cardiac_status = get_valid_standard_single(
        "cardiac_status",
        "Please enter the cardiac status: "
    )

    respiratory_status = get_valid_standard_single(
        "respiratory_status",
        "Please enter the respiratory status: "
    )

    neurological_status = get_valid_standard_single(
        "neurological_status",
        "Please enter the neurological status: "
    )

    lab_instability = get_valid_standard_single(
        "lab_instability",
        "Please enter the lab instability status: "
    )

    safety_risk = get_valid_standard_single(
        "safety_risk",
        "Please enter the safety risk: "
    )

    behaviour_cooperation = get_valid_standard_single(
        "behaviour_cooperation",
        "Please enter the behaviour/cooperation status: "
    )

    medication_complexity = get_valid_standard_single(
        "medication_complexity",
        "Please enter the medication complexity: "
    )

    cbgm_frequency = get_valid_standard_single(
        "cbgm_frequency",
        "Please enter the CBGM frequency: "
    )

    monitoring_frequency = get_valid_standard_single(
        "monitoring_frequency",
        "Please enter the monitoring frequency: "
    )

    iv_access = get_valid_standard_single(
        "iv_access",
        "Please enter the IV access: "
    )

    nutrition = get_valid_standard_single(
        "nutrition",
        "Please enter the nutrition status: "
    )

    wounds_dressings = get_valid_standard_single(
        "wounds_dressings",
        "Please enter the wounds/dressings status: "
    )

    elimination = get_valid_standard_single(
        "elimination",
        "Please enter the elimination status: "
    )

    mobility = get_valid_standard_single(
        "mobility",
        "Please enter the mobility status: "
    )

    pain_management = get_valid_standard_single(
        "pain_management",
        "Please enter the pain management status: "
    )

    communication = get_valid_standard_single(
        "communication",
        "Please enter the communication status: "
    )

    family_social = get_valid_standard_single(
        "family_social",
        "Please enter the family/social status: "
    )

    blood_test_frequency = get_valid_standard_single(
        "blood_test_frequency",
        "Please enter the blood test frequency: "
    )

    medications = get_list_input(
        "Please enter the medication list (comma separated): "
    )

    issues = get_list_input(
        "Please enter the current issues (comma separated): "
    )

    plans = get_nonempty_input("Please enter the plan: ").strip().upper()

    pro_involved = get_valid_standard_multi(
        "pro_involved",
        "Please enter the professionals involved (comma separated): "
    )

    home_screen = get_nonempty_input("Please enter the home situation: ").strip().upper()

    turnover = get_valid_standard_single(
        "turnover",
        "Please enter the turnover status: "
    )

    special_flags = get_list_input(
        "Please enter any special flags (comma separated, or press Enter for none): "
    )
    special_flags = [flag.strip().upper() for flag in special_flags]

    patient = patient_info.Patient(
        unit=unit,
        room=room,
        name=name,
        mrn=mrn,
        age=age,
        gender=gender,
        admission_date=admission_date,
        team_doctor=team_doctor,
        diagnosis=diagnosis,

        isolation_status=isolation_status,
        level_of_intervention=level_of_intervention,
        pmhx=pmhx,
        allergies=allergies,
        type_sx=type_sx,
        procedures_tests=procedures_tests,

        hemodynamic_status=hemodynamic_status,
        cardiac_status=cardiac_status,
        respiratory_status=respiratory_status,
        neurological_status=neurological_status,
        lab_instability=lab_instability,
        safety_risk=safety_risk,
        behaviour_cooperation=behaviour_cooperation,
        medication_complexity=medication_complexity,
        cbgm_frequency=cbgm_frequency,
        monitoring_frequency=monitoring_frequency,

        iv_access=iv_access,
        nutrition=nutrition,
        wounds_dressings=wounds_dressings,
        elimination=elimination,
        mobility=mobility,
        pain_management=pain_management,
        communication=communication,
        family_social=family_social,
        blood_test_frequency=blood_test_frequency,

        medications=medications,
        issues=issues,
        plans=plans,
        pro_involved=pro_involved,
        home_screen=home_screen,
        turnover=turnover,
        vital_signs=None,
        special_flags=special_flags
    )

    #Adding the Acuity Score to this patient 
    scores = get_patient_assignment_score(patient)
    patient.acuity_score = scores["acuity_weighted"]
    patient.workload_score = scores["workload_weighted"]
    patient.modifier_score = scores["modifiers_weighted"]
    patient.total_raw_score = scores["total_raw"]
    patient.total_weighted_score = scores["total_weighted"]
    patient.score_breakdown = scores

    #Printing this after getting a patient scored
    print("\n--- PATIENT AUTOMATICALLY SCORED ---")
    print(f"Acuity Raw: {scores['acuity_raw']}")
    print(f"Workload Raw: {scores['workload_raw']}")
    print(f"Modifiers Raw: {scores['modifiers_raw']}")
    print(f"Total Weighted Score: {scores['total_weighted']}")

    #Adding this patient on this unit
    cardiology_units[unit][mrn] = patient

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

    occupied_rooms = {
        existing_patient.room for existing_patient in cardiology_units[destination_unit].values()
    }

    if destination_unit == current_unit:
        occupied_rooms.discard(patient.room)

    available_rooms = valid_rooms[destination_unit] - occupied_rooms

    if not available_rooms:
        print(f"No available rooms in {destination_unit}.")
        return

    print(f"\nAvailable rooms in {destination_unit}:")
    for room in sorted(available_rooms):
        print(room)

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

# Refreshing the patient's score/ After updating the patient's information
def refresh_patient_score(patient):
    scores = get_patient_assignment_score(patient)

    patient.acuity_score = scores["acuity_weighted"]
    patient.workload_score = scores["workload_weighted"]
    patient.modifier_score = scores["modifiers_weighted"]

    patient.total_raw_score = scores["total_raw"]
    patient.total_weighted_score = scores["total_weighted"]

    patient.score_breakdown = scores

# Updating a patient's information as needed 
def update_pt_information(cardiology_units):

    current_unit = input("Enter the current unit (CVICU or CVU): ").strip().upper()

    if current_unit not in cardiology_units:
        print("Invalid current unit.")
        return

    patient_mrn = int(input("Enter the MRN of the patient you want to update: "))

    if patient_mrn not in cardiology_units[current_unit]:
        print("No patient found with that MRN in this unit.")
        return

    patient = cardiology_units[current_unit][patient_mrn]

    while True:
        choice = pt_update_menu()

        if choice is None:
            continue

        if choice == 1:
            patient.team_doctor = get_nonempty_input("Enter the new doctor/team: ").strip().upper()
            print("Doctor updated successfully.")
            refresh_patient_score(patient)

        elif choice == 2:
            patient.diagnosis = get_valid_standard_single(
                "diagnosis",
                "Enter the new diagnosis: "
            )
            print("Diagnosis updated successfully.")
            refresh_patient_score(patient)

        elif choice == 3:
            patient.isolation_status = get_valid_standard_single(
                "isolation_status",
                "Enter the new isolation status: "
            )
            print("Isolation status updated successfully.")
            refresh_patient_score(patient)

        elif choice == 4:
            patient.level_of_intervention = get_valid_standard_single(
                "level_of_intervention",
                "Enter the new level of intervention: "
            )
            print("Level of intervention updated successfully.")
            refresh_patient_score(patient)

        elif choice == 5:
            patient.pmhx = get_valid_standard_multi(
                "pmhx",
                "Enter the updated past medical history (comma separated): "
            )
            print("Past medical history updated successfully.")
            refresh_patient_score(patient)

        elif choice == 6:
            patient.allergies = get_list_input(
                "Enter the updated allergies (comma separated): "
            )
            print("Allergies updated successfully.")
            refresh_patient_score(patient)

        elif choice == 7:
            patient.type_sx = get_nonempty_input("Enter the updated type of surgery: ").strip().upper()
            print("Type of surgery updated successfully.")
            refresh_patient_score(patient)

        elif choice == 8:
            patient.procedures_tests = get_valid_standard_multi(
                "procedures_tests",
                "Enter the updated procedures/tests (comma separated): "
            )
            print("Procedures/tests updated successfully.")
            refresh_patient_score(patient)

        elif choice == 9:
            patient.hemodynamic_status = get_valid_standard_single(
                "hemodynamic_status",
                "Enter the updated hemodynamic status: "
            )
            print("Hemodynamic status updated successfully.")
            refresh_patient_score(patient)

        elif choice == 10:
            patient.cardiac_status = get_valid_standard_single(
                "cardiac_status",
                "Enter the updated cardiac status: "
            )
            print("Cardiac status updated successfully.")
            refresh_patient_score(patient)

        elif choice == 11:
            patient.respiratory_status = get_valid_standard_single(
                "respiratory_status",
                "Enter the updated respiratory status: "
            )
            print("Respiratory status updated successfully.")
            refresh_patient_score(patient)

        elif choice == 12:
            patient.neurological_status = get_valid_standard_single(
                "neurological_status",
                "Enter the updated neurological status: "
            )
            print("Neurological status updated successfully.")
            refresh_patient_score(patient)

        elif choice == 13:
            patient.lab_instability = get_valid_standard_single(
                "lab_instability",
                "Enter the updated lab instability: "
            )
            print("Lab instability updated successfully.")
            refresh_patient_score(patient)

        elif choice == 14:
            patient.safety_risk = get_valid_standard_single(
                "safety_risk",
                "Enter the updated safety risk: "
            )
            print("Safety risk updated successfully.")
            refresh_patient_score(patient)

        elif choice == 15:
            patient.behaviour_cooperation = get_valid_standard_single(
                "behaviour_cooperation",
                "Enter the updated behaviour/cooperation: "
            )
            print("Behaviour/cooperation updated successfully.")
            refresh_patient_score(patient)

        elif choice == 16:
            patient.medication_complexity = get_valid_standard_single(
                "medication_complexity",
                "Enter the updated medication complexity: "
            )
            print("Medication complexity updated successfully.")
            refresh_patient_score(patient)

        elif choice == 17:
            patient.cbgm_frequency = get_valid_standard_single(
                "cbgm_frequency",
                "Enter the updated CBGM frequency: "
            )
            print("CBGM frequency updated successfully.")
            refresh_patient_score(patient)

        elif choice == 18:
            patient.monitoring_frequency = get_valid_standard_single(
                "monitoring_frequency",
                "Enter the updated monitoring frequency: "
            )
            print("Monitoring frequency updated successfully.")
            refresh_patient_score(patient)

        elif choice == 19:
            patient.iv_access = get_valid_standard_single(
                "iv_access",
                "Enter the updated IV access: "
            )
            print("IV access updated successfully.")
            refresh_patient_score(patient)

        elif choice == 20:
            patient.nutrition = get_valid_standard_single(
                "nutrition",
                "Enter the updated nutrition: "
            )
            print("Nutrition updated successfully.")
            refresh_patient_score(patient)

        elif choice == 21:
            patient.wounds_dressings = get_valid_standard_single(
                "wounds_dressings",
                "Enter the updated wounds/dressings: "
            )
            print("Wounds/dressings updated successfully.")
            refresh_patient_score(patient)

        elif choice == 22:
            patient.elimination = get_valid_standard_single(
                "elimination",
                "Enter the updated elimination status: "
            )
            print("Elimination updated successfully.")
            refresh_patient_score(patient)

        elif choice == 23:
            patient.mobility = get_valid_standard_single(
                "mobility",
                "Enter the updated mobility status: "
            )
            print("Mobility updated successfully.")
            refresh_patient_score(patient)

        elif choice == 24:
            patient.pain_management = get_valid_standard_single(
                "pain_management",
                "Enter the updated pain management: "
            )
            print("Pain management updated successfully.")
            refresh_patient_score(patient)

        elif choice == 25:
            patient.communication = get_valid_standard_single(
                "communication",
                "Enter the updated communication status: "
            )
            print("Communication updated successfully.")
            refresh_patient_score(patient)

        elif choice == 26:
            patient.family_social = get_valid_standard_single(
                "family_social",
                "Enter the updated family/social status: "
            )
            print("Family/social updated successfully.")
            refresh_patient_score(patient)

        elif choice == 27:
            patient.blood_test_frequency = get_valid_standard_single(
                "blood_test_frequency",
                "Enter the updated blood test frequency: "
            )
            print("Blood test frequency updated successfully.")
            refresh_patient_score(patient)

        elif choice == 28:
            patient.medications = get_list_input(
                "Enter the updated medications (comma separated): "
            )
            print("Medications updated successfully.")
            refresh_patient_score(patient)

        elif choice == 29:
            patient.issues = get_list_input(
                "Enter the updated issues (comma separated): "
            )
            print("Issues updated successfully.")
            refresh_patient_score(patient)

        elif choice == 30:
            patient.plans = get_nonempty_input("Enter the updated plans: ").strip().upper()
            print("Plans updated successfully.")
            refresh_patient_score(patient)

        elif choice == 31:
            patient.pro_involved = get_valid_standard_multi(
                "pro_involved",
                "Enter the updated professionals involved (comma separated): "
            )
            print("Professionals involved updated successfully.")
            refresh_patient_score(patient)

        elif choice == 32:
            patient.home_screen = get_nonempty_input("Enter the updated home situation: ").strip().upper()
            print("Home situation updated successfully.")
            refresh_patient_score(patient)

        elif choice == 33:
            patient.turnover = get_valid_standard_single(
                "turnover",
                "Enter the updated turnover status: "
            )
            print("Turnover updated successfully.")
            refresh_patient_score(patient)

        elif choice == 34:
            patient.special_flags = get_list_input(
                "Enter the updated special flags (comma separated): "
            )
            patient.special_flags = [flag.strip().upper() for flag in patient.special_flags]
            print("Special flags updated successfully.")
            refresh_patient_score(patient)

        elif choice == 35:
            print("Returning to main menu.")
            break

# Viewing all the patient's on the unit
def view_all_patients (cardiology_units):
    
    has_patients = False
    
    for unit, patients in cardiology_units.items():
        print(f"\n---             {unit}                  ---")
        print(f"---{unit} current has ({len(patients)}) patients --- ")

        if not patients:
            print("\nThere are no patients currently on the unit.")
        else:
            for patient in patients.values():
                print(f"Room: {patient.room} | Name: {patient.name} | MRN: {patient.mrn} | Diagnosis: {patient.diagnosis}")
            print("-" * 40)

# Viewing all the patients with full information by unit
def view_all_patients_with_info(cardiology_units):

    has_patients = False

    for unit, patients in cardiology_units.items():

        print(f"\n---                 {unit}                      ---")
        print(f"---{unit} current has ({len(patients)}) patients --- ")

        if not patients:
            print("No patients in this unit.")
        else:
            has_patients = True
            for patient in patients.values():
                patient.display_info()
                print("-" * 40)

    if not has_patients:
        print("\nThere are no patients currently in any unit.")

# Viewing all of the information of one patient
def view_one_patient_info(cardiology_units):
    
    mrn = int(input("Enter the MRN of the patient you want to view: "))
    
    for unit, patients in cardiology_units.items():

        if mrn in patients:
            
            patient = patients[mrn]
            print(f"\n--Patient found in {unit} ---")
            patient.display_info()
            return
        
    print("\nPatient not found.")

# Updating the vital signs of a patient in the unit
def update_vital_signs(cardiology_units):

    mrn = int(input("Enter the patient's MRN: "))

    for unit, patients in cardiology_units.items():

        if mrn in patients:
            
            patient = patients[mrn]
            print(f"\n--Patient found in {unit} ---")
            print(f"Name: {patient.name} | Room: {patient.room}")
            
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
            return  
    
    print("\nPatient not found")

# Viewing the lastest vital_signs of a patient in the unit
def view_latest_vital_signs(cardiology_units):
    
    mrn = int(input("Enter the patient's MRN: "))

    for unit, patients in cardiology_units.items():

        if mrn in patients:

            patient = patients[mrn]
            print(f"\n--Patient found in {unit} ---")
            print(f"Name: {patient.name} | Room: {patient.room}")

            if patient.vital_signs is None:
                print("No vital signs recorded yet.")
                return

            print(f"\nLatest vital signs for {patient.room} {patient.name}, MRN: {patient.mrn}:")
            patient.vital_signs.display_vitals()
            return
    
    print("\nPatient not found")

# Checking if the room is occupied:
def is_room_occupied(unit_patients, room):
    for patient in unit_patients.values():
        if patient.room == room:
            return True
    return False

# Checking if a room is available
def check_available_rooms(cardiology_units, valid_rooms):
    print("\n--- ROOM STATUS ---")

    for unit in ["CVICU", "CVU"]:
        print(f"\n{unit}:")

        room_to_patient = {}
        for patient in cardiology_units[unit].values():
            room_to_patient[patient.room] = patient.name

        available_rooms = []
        full_rooms = []

        for room in sorted(valid_rooms[unit]):
            if room in room_to_patient:
                full_rooms.append(f"{room} ({room_to_patient[room]})")
            else:
                available_rooms.append(room)

        print(f"Available rooms: {', '.join(available_rooms) if available_rooms else 'None'}")
        print(f"Full rooms: {', '.join(full_rooms) if full_rooms else 'None'}")
        print(f"Total available: {len(available_rooms)}")
        print(f"Total full: {len(full_rooms)}")

#___SCORING SECTION_____
#Can use this to view patient_scores and refresh all patient scores when needed 
def score_all_patients(cardiology_units):
    for unit, patients in cardiology_units.items():
        for patient in patients.values():
            refresh_patient_score(patient)

    print("All patients scored successfully.")

# Viewing patients by acuity level
def view_patients_by_acuity(cardiology_units):

    all_patients = []

    for unit, patients in cardiology_units.items():
        for patient in patients.values():
            all_patients.append((patient.acuity_score, unit, patient))

    if not all_patients:
        print("No patients found.")
        return

    all_patients.sort(reverse=True, key=lambda x: x[0])

    print("\n--- PATIENTS SORTED BY ACUITY SCORE ---")

    for score, unit, patient in all_patients:
        print(
            f"{patient.name} | {unit} | Room: {patient.room} | "
            f"Acuity: {patient.acuity_score} | "
            f"Workload: {patient.workload_score} | "
            f"Modifier: {patient.modifier_score} | "
            f"Total: {patient.total_weighted_score}"
        )

#Viewing patients by total heaviest assignment
def view_patients_by_total_score(cardiology_units):

    all_patients = []

    for unit, patients in cardiology_units.items():
        for patient in patients.values():
            all_patients.append((patient.total_weighted_score, unit, patient))

    if not all_patients:
        print("No patients found.")
        return

    all_patients.sort(reverse=True, key=lambda x: x[0])

    print("\n--- PATIENTS SORTED BY TOTAL WEIGHTED SCORE ---")

    for score, unit, patient in all_patients:
        print(
            f"{patient.name} | {unit} | Room: {patient.room} | "
            f"Acuity: {patient.acuity_score} | "
            f"Workload: {patient.workload_score} | "
            f"Modifier: {patient.modifier_score} | "
            f"Total: {patient.total_weighted_score}"
        )

#___________________________________________________________
#Main Driver
def main():
    welcome()

    while True:
        menu_choice = menu()

        if menu_choice is None:
            continue

        match menu_choice:

            case 1:
                print("Admit a patient")
                admit_patient(cardiology_units, unit_capacities, valid_rooms)
                print("*" * 40)

            case 2:
                print("Discharging a patient")
                discharge_patient(cardiology_units)
                print("*" * 40)

            case 3:
                print("Transferring a patient to another unit")
                transfer_patient(cardiology_units, unit_capacities, valid_rooms)
                print("*" * 40)

            case 4:
                print("Updating patient information")
                update_pt_information(cardiology_units)
                print("*" * 40)

            case 5:
                print("Viewing all the patients")
                view_all_patients(cardiology_units)
                print("*" * 40)

            case 6:
                print("Viewing all the patients with information")
                view_all_patients_with_info(cardiology_units)
                print("*" * 40)

            case 7:
                print("Viewing one patient")
                view_one_patient_info(cardiology_units)
                print("*" * 40)

            case 8:
                print("Update one patient's vital signs")
                update_vital_signs(cardiology_units)
                print("*" * 40)

            case 9:
                print("View one patient's vital signs")
                view_latest_vital_signs(cardiology_units)
                print("*" * 40)

            case 10:
                print("Viewing CVU/CVICU Bedflow")
                check_available_rooms(cardiology_units, valid_rooms)
                print("*" * 40)

            case 11:
                print("Viewing patients ranked by acuity")
                view_patients_by_acuity(cardiology_units)
                print("*" * 40)

            case 12:
                print("Viewing patients ranked by total weighted score")
                view_patients_by_total_score(cardiology_units)
                print("*" * 40)

            case 13:
                print("Exiting")
                break

            case _:
                print("Invalid choice. Try again!")

    print("Thank you for visiting the unit! Application now closing")


if __name__ == "__main__":
    main()

    