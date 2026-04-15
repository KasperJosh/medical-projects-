from nurse_profile import Nurse
from assignment_engine import assign_patients_to_nurses, detect_unsafe_assignments
from patient_info import Patient


# ---- Create nurses ----
nurses = [
    Nurse(
        "Rina", 1, "Expert", ["BLS", "ACLS", "CRRT", "IABP"],
        18, 3,
        False, 12, 8,
        can_take_admission=True,
        empty_rooms_assigned=1,
        learning_needs=[],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Neda", 2, "Expert", ["BLS", "ACLS"],
        16, 3,
        False, 10, 6,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=["POST_CATH"],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Arete", 3, "Intermediate", ["BLS", "ACLS"],
        14, 3,
        False, 5, 2,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=["CARDIAC_DRIPS", "POST_CATH"],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Celine", 4, "Beginner", ["BLS"],
        10, 2,
        True, 1, 0.5,
        can_take_admission=False,
        empty_rooms_assigned=0,
        learning_needs=["TELEMETRY", "POST_CATH"],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Bharati", 5, "Expert", ["BLS", "ACLS", "CRRT", "IABP"],
        18, 3,
        False, 15, 10,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=[],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Eugenie", 6, "Expert", ["BLS", "ACLS"],
        16, 3,
        False, 8, 5,
        can_take_admission=True,
        empty_rooms_assigned=1,
        learning_needs=["CHEST_TUBES"],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Nancy", 7, "Intermediate", ["BLS", "ACLS"],
        14, 3,
        False, 4, 1.5,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=["CARDIAC_DRIPS"],
        refused_patients=[],
        is_light_duty=False
    ),

    Nurse(
        "Azam", 8, "Beginner", ["BLS"],
        10, 2,
        True, 1, 0.25,
        can_take_admission=False,
        empty_rooms_assigned=0,
        learning_needs=["POST_CATH", "DISCHARGE_TEACHING"],
        refused_patients=[],
        is_light_duty=False
    ),
]


# ---- Create patients ----
patient1 = Patient(
    unit ="CVU",room="K0201", name="Jean Tremblay", mrn=1001, age=72, gender="M",
    admission_date="2026-04-15",
    isolation_status="NONE", level_of_intervention="A", team_doctor="Dr. Smith",
    diagnosis="NSTEMI",
    pmhx=["HTN", "DM2"], allergies=[],
    type_sx="NONE", procedures_tests=["CATH"],
    cardiac_status="AFIB", respiratory_status="NP",
    iv_access="PIV", nutrition="DM_CBGM",
    wounds_dressings="PRIMAPORE_STERNUM", elimination="FOLEY",
    mobility="SUPERVISION", lab_instability="ROUTINE",
    medications=["HEPARIN"],
    issues=["FALL_RISK"], plans=["ECHO"],
    pro_involved=["PT"], home_screen="LIVES_ALONE",
    turnover="STABLE",
    acuity_score=7, total_weighted_score=9
)

patient2 = Patient(
    unit ="CVU",room="K0202", name="Maria Lopez", mrn=1002, age=65, gender="F",
    admission_date="2026-04-15",
    isolation_status="CONTACT", level_of_intervention="A", team_doctor="Dr. Brown",
    diagnosis="STEMI",
    pmhx=["CAD"], allergies=[],
    type_sx="CABG", procedures_tests=["CXR"],
    cardiac_status="VT", respiratory_status="BIPAP",
    iv_access="CVAD", nutrition="NPO",
    wounds_dressings="COMPLEX_DRESSING", elimination="FOLEY",
    mobility="BEDREST", lab_instability="Q4H",
    medications=["AMIODARONE"],
    issues=["FALL_RISK"], plans=["ICU"],
    pro_involved=["RT"], home_screen="UNKNOWN",
    turnover="NEW_ADMISSION",
    acuity_score=10, total_weighted_score=12
)

patient3 = Patient(
    unit ="CVU",room="K0203", name="Sarah Nguyen", mrn=1003, age=80, gender="F",
    admission_date="2026-04-15",
    isolation_status="NONE", level_of_intervention="C", team_doctor="Dr. Lee",
    diagnosis="CHF",
    pmhx=["HTN"], allergies=[],
    type_sx="NONE", procedures_tests=[],
    cardiac_status="NSR", respiratory_status="RA",
    iv_access="NONE", nutrition="REGULAR",
    wounds_dressings="NONE", elimination="TOILET",
    mobility="ASSIST_X2", lab_instability="DAILY",
    medications=["DIURETIC"],
    issues=["CONFUSED"], plans=["DC_SOON"],
    pro_involved=["SW"], home_screen="LIVES_ALONE",
    turnover="STABLE",
    acuity_score=3, total_weighted_score=8
)

patient_list = [patient1, patient2, patient3]


# ---- Run assignment ----
assigned_nurses, unassigned = assign_patients_to_nurses(patient_list, nurses)


# ---- Display ----
warnings = detect_unsafe_assignments(assigned_nurses)

print("\n=== ASSIGNMENT RESULTS ===")
for nurse in assigned_nurses:
    nurse.display_assignment()

if unassigned:
    print("\n=== UNASSIGNED PATIENTS ===")
    for patient in unassigned:
        print(f" - Room {patient.room}: {patient.name}")
else:
    print("\nAll patients assigned successfully.")

if warnings:
    print("\n=== UNSAFE / QUESTIONABLE ASSIGNMENTS ===")
    for warning in warnings:
        print(f" - {warning}")
else:
    print("\nNo unsafe assignments detected.")