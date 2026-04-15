from nurse_profile import Nurse
from assignment_engine import assign_patients_to_nurses
from patient_info import Patient


# ---- Create nurses ----
nurses = [
    Nurse("Rina", 1, "Expert", ["ACLS", "CRRT", "IABP"], 18, 3),
    Nurse("Neda", 2, "Expert", ["ACLS"], 16, 3),
    Nurse("Arete", 3, "Intermediate", ["ACLS"], 14, 3),
    Nurse("Celine", 4, "Beginner", ["BLS"], 10, 2),
    Nurse("Bharati", 1, "Expert", ["ACLS", "CRRT", "IABP"], 18, 3),
    Nurse("Eugenie", 2, "Expert", ["ACLS"], 16, 3),
    Nurse("Nancy", 3, "Intermediate", ["ACLS"], 14, 3),
    Nurse("Azam", 4, "Beginner", ["BLS"], 10, 2),
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
    turnover="NO",
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
    turnover="NO",
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
    turnover="YES",
    acuity_score=3, total_weighted_score=8
)

patient_list = [patient1, patient2, patient3]


# ---- Run assignment ----
assigned_nurses, unassigned = assign_patients_to_nurses(patient_list, nurses)


# ---- Display ----
print("\n=== ASSIGNMENT RESULTS ===")
for nurse in assigned_nurses:
    nurse.display_assignment()

if unassigned:
    print("\n=== UNASSIGNED PATIENTS ===")
    for p in unassigned:
        print(f" - {p.name}")
else:
    print("\nAll patients assigned successfully.")