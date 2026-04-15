# Defining functions for the nurse patient load 

def nurse_load_score(nurse):
    return (nurse.current_acuity * 2) + nurse.current_weighted


def assign_patients_to_nurses(patients, nurses):
    unassigned_patients = []

    sorted_patients = sorted(patients, key=lambda p: p.acuity_score, reverse=True)

    for patient in sorted_patients:
        eligible_nurses = [nurse for nurse in nurses if nurse.can_take_patient(patient)]

        if not eligible_nurses:
            unassigned_patients.append(patient)
            continue

        best_nurse = min(eligible_nurses, key=nurse_load_score)
        best_nurse.assign_patient(patient)

    return nurses, unassigned_patients