from nurse_profile import Nurse
from assignment_engine import assign_patients_to_nurses, detect_unsafe_assignments
from patient_info import Patient


# ---- Create nurses ----
nurses = [
    Nurse(
        "Rina", 1, "Expert", ["BLS", "ACLS", "CRRT", "IABP"],
        18, 3, False, 12, 8,
        can_take_admission=True,
        empty_rooms_assigned=1,
        learning_needs=[],
        refused_patients=[],
        is_light_duty=False,
        pod="B"
    ),

    Nurse(
        "Neda", 2, "Expert", ["BLS", "ACLS"],
        16, 3, False, 10, 6,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=["POST_CATH"],
        refused_patients=[],
        is_light_duty=False,
        pod="B"
    ),

    Nurse(
        "Arete", 3, "Intermediate", ["BLS", "ACLS"],
        14, 3, False, 5, 2,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=["CARDIAC_DRIPS", "POST_CATH"],
        refused_patients=[],
        is_light_duty=False,
        pod="B"
    ),

    Nurse(
        "Celine", 4, "Beginner", ["BLS"],
        10, 2, False, 1, 0.5,
        can_take_admission=False,
        empty_rooms_assigned=0,
        learning_needs=["TELEMETRY", "POST_CATH"],
        refused_patients=[],
        is_light_duty=False,
        pod="B"
    ),

    Nurse(
        "Bharati", 5, "Expert", ["BLS", "ACLS", "CRRT", "IABP"],
        18, 3, False, 15, 10,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=[],
        refused_patients=[],
        is_light_duty=False,
        pod="C"
    ),

    Nurse(
        "Eugenie", 6, "Expert", ["BLS", "ACLS"],
        16, 3, False, 8, 5,
        can_take_admission=True,
        empty_rooms_assigned=1,
        learning_needs=["CHEST_TUBES"],
        refused_patients=[],
        is_light_duty=False,
        pod="C"
    ),

    Nurse(
        "Nancy", 7, "Intermediate", ["BLS", "ACLS"],
        14, 3, False, 4, 1.5,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=["CARDIAC_DRIPS"],
        refused_patients=[],
        is_light_duty=False,
        pod="C"
    ),

    Nurse(
        "Azam", 8, "Beginner", ["BLS"],
        10, 2, True, 1, 0.25,
        can_take_admission=False,
        empty_rooms_assigned=0,
        learning_needs=["POST_CATH", "DISCHARGE_TEACHING"],
        refused_patients=[],
        is_light_duty=False,
        pod="C"
    ),
]


# ---- Create patients ----
# -------- POD B --------

patient1 = Patient(
    unit="CVU", room="K0210", name="P1", mrn=2001, age=70, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="NSTEMI",
    isolation_status="NONE", level_of_intervention="A",
    type_sx="NONE", procedures_tests=["CATH"],
    hemodynamic_status="STABLE", cardiac_status="AFIB", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="FALL_RISK", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="DM_CBGM", wounds_dressings="NONE",
    elimination="FOLEY", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=1,
    acuity_score=7, total_weighted_score=9
)

patient2 = Patient(
    unit="CVU", room="K0211", name="P2", mrn=2002, age=65, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="STEMI",
    isolation_status="NONE", level_of_intervention="A",
    type_sx="CABG", procedures_tests=["CXR"],
    hemodynamic_status="UNSTABLE", cardiac_status="VT", respiratory_status="BIPAP",
    neurological_status="AOX3", lab_instability="Q4H",
    safety_risk="FALL_RISK", behaviour_cooperation="ANXIOUS",
    medication_complexity="IV_COMPLEX", cbgm_frequency="Q1H",
    monitoring_frequency="CONTINUOUS",
    iv_access="CVAD", nutrition="NPO", wounds_dressings="COMPLEX_DRESSING",
    elimination="FOLEY", mobility="BEDREST",
    pain_management="CONTROLLED",
    turnover="NEW_ADMISSION", previous_nurse_id=2,
    acuity_score=10, total_weighted_score=12
)

patient3 = Patient(
    unit="CVU", room="K0214", name="P3", mrn=2003, age=80, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="CHF",
    isolation_status="NONE", level_of_intervention="C",
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="RA",
    neurological_status="AOX2", lab_instability="DAILY",
    safety_risk="NONE", behaviour_cooperation="CONFUSED",
    medication_complexity="PO", cbgm_frequency="DAILY",
    monitoring_frequency="ROUTINE",
    iv_access="NONE", nutrition="REGULAR", wounds_dressings="NONE",
    elimination="TOILET", mobility="ASSIST_X2",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=3,
    acuity_score=3, total_weighted_score=6
)

patient4 = Patient(
    unit="CVU", room="K0220", name="P4", mrn=2004, age=77, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="ARRHYTHMIA",
    isolation_status="NONE", level_of_intervention="A",
    hemodynamic_status="STABLE", cardiac_status="AFIB", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="FALL_RISK", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="URINAL", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="TRANSFER_TODAY", previous_nurse_id=1,
    acuity_score=6, total_weighted_score=8
)

patient5 = Patient(
    unit="CVU", room="K0225", name="P5", mrn=2005, age=60, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="STEMI",
    isolation_status="CONTACT", level_of_intervention="A",
    type_sx="CABG", procedures_tests=["CXR"],
    hemodynamic_status="UNSTABLE", cardiac_status="VT", respiratory_status="BIPAP",
    neurological_status="AOX3", lab_instability="Q4H",
    safety_risk="FALL_RISK", behaviour_cooperation="ANXIOUS",
    medication_complexity="IV_COMPLEX", cbgm_frequency="Q1H",
    monitoring_frequency="CONTINUOUS",
    iv_access="CVAD", nutrition="NPO", wounds_dressings="COMPLEX_DRESSING",
    elimination="FOLEY", mobility="BEDREST",
    pain_management="CONTROLLED",
    turnover="NEW_ADMISSION", previous_nurse_id=2,
    acuity_score=10, total_weighted_score=12
)

patient6 = Patient(
    unit="CVU", room="K0226", name="P6", mrn=2006, age=72, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="POST_CATH",
    procedures_tests=["CATH"],
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="DM_CBGM", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="POSSIBLE_TRANSFER", previous_nurse_id=3,
    acuity_score=5, total_weighted_score=7
)

patient7 = Patient(
    unit="CVU", room="K0230", name="P7", mrn=2007, age=68, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="CHF",
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="DAILY",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="PO", cbgm_frequency="DAILY",
    monitoring_frequency="ROUTINE",
    iv_access="NONE", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="TOILET", mobility="ASSIST_X1",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=4,
    acuity_score=4, total_weighted_score=6
)

patient8 = Patient(
    unit="CVU", room="K0255", name="P8", mrn=2008, age=75, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="POST_OP",
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="FALL_RISK", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="FOLEY", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="DISCHARGE_TODAY", previous_nurse_id=1,
    acuity_score=5, total_weighted_score=7
)

# -------- POD C --------

patient9 = Patient(
    unit="CVU", room="K0231", name="P9", mrn=2009, age=76, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="CHF",
    procedures_tests=["TTE"],
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    family_social="FAMILY",
    turnover="TRANSFER_TODAY", previous_nurse_id=5,
    acuity_score=6, total_weighted_score=9
)

patient10 = Patient(
    unit="CVU", room="K0232", name="P10", mrn=2010, age=70, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="NSTEMI",
    hemodynamic_status="STABLE", cardiac_status="AFIB", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="FALL_RISK", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=6,
    acuity_score=5, total_weighted_score=7
)

patient11 = Patient(
    unit="CVU", room="K0240", name="P11", mrn=2011, age=85, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="CHF",
    level_of_intervention="C",
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="RA",
    neurological_status="AOX2", lab_instability="DAILY",
    safety_risk="NONE", behaviour_cooperation="CONFUSED",
    medication_complexity="PO", cbgm_frequency="DAILY",
    monitoring_frequency="ROUTINE",
    iv_access="NONE", nutrition="REGULAR", wounds_dressings="NONE",
    elimination="TOILET", mobility="ASSIST_X2",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=7,
    acuity_score=3, total_weighted_score=6
)

patient12 = Patient(
    unit="CVU", room="K0244", name="P12", mrn=2012, age=65, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="POST_CATH",
    procedures_tests=["CATH"],
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="DM_CBGM", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="POSSIBLE_TRANSFER", previous_nurse_id=5,
    acuity_score=5, total_weighted_score=7
)

patient13 = Patient(
    unit="CVU", room="K0250", name="P13", mrn=2013, age=72, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="ARRHYTHMIA",
    hemodynamic_status="STABLE", cardiac_status="AFIB", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=6,
    acuity_score=5, total_weighted_score=7
)

patient14 = Patient(
    unit="CVU", room="K0251", name="P14", mrn=2014, age=68, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="CHF",
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="DAILY",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="PO", cbgm_frequency="DAILY",
    monitoring_frequency="ROUTINE",
    iv_access="NONE", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="TOILET", mobility="ASSIST_X1",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=7,
    acuity_score=4, total_weighted_score=6
)

patient15 = Patient(
    unit="CVU", room="K0254", name="P15", mrn=2015, age=69, gender="F",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="POST_CATH",
    procedures_tests=["CATH"],
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="DM_CBGM", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="STABLE", previous_nurse_id=8,
    acuity_score=4, total_weighted_score=6
)

patient16 = Patient(
    unit="CVU", room="K0271", name="P16", mrn=2016, age=78, gender="M",
    admission_date="2026-04-15", team_doctor="Dr", diagnosis="CHF",
    hemodynamic_status="STABLE", cardiac_status="NSR", respiratory_status="NP",
    neurological_status="AOX3", lab_instability="ROUTINE",
    safety_risk="NONE", behaviour_cooperation="COOPERATIVE",
    medication_complexity="IV_SIMPLE", cbgm_frequency="ACHS",
    monitoring_frequency="ENHANCED",
    iv_access="PIV", nutrition="CARDIAC", wounds_dressings="NONE",
    elimination="TOILET", mobility="SUPERVISION",
    pain_management="CONTROLLED",
    turnover="NEW_ADMISSION", previous_nurse_id=5,
    acuity_score=7, total_weighted_score=9
)


patient_list = [
    patient1, patient2, patient3, patient4,
    patient5, patient6, patient7, patient8,
    patient9, patient10, patient11, patient12,
    patient13, patient14, patient15, patient16
]

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