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
patient1 = Patient("CVU","K0210","P1",2001,70,"M","2026-04-15","NONE","A","Dr",
"NSTEMI",[],[],"NONE",["CATH"],
"AFIB","NP","AOX3","ROUTINE","FALL_RISK","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","DM_CBGM",
"FOLEY",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=7, total_weighted_score=9)

patient2 = Patient("CVU","K0211","P2",2002,65,"F","2026-04-15","NONE","A","Dr",
"STEMI",[],[],"CABG",["CXR"],
"VT","BIPAP","AOX3","Q4H","FALL_RISK","ANXIOUS",
"IV_COMPLEX","Q1H","CONTINUOUS","CVAD","BEDREST","NPO",
"FOLEY",[], "COMPLEX_DRESSING","CONTROLLED","NONE","FAMILY","DAILY",
"NONE","NEW_ADMISSION",[], "", False, acuity_score=10, total_weighted_score=12)

patient3 = Patient("CVU","K0214","P3",2003,80,"F","2026-04-15","NONE","C","Dr",
"CHF",[],[],"NONE",[],
"NSR","RA","AOX2","DAILY","NONE","CONFUSED",
"PO","DAILY","ROUTINE","NONE","ASSIST_X2","REGULAR",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=3, total_weighted_score=6)

patient4 = Patient("CVU","K0220","P4",2004,77,"M","2026-04-15","NONE","A","Dr",
"ARRHYTHMIA",[],[],"NONE",[],
"AFIB","NP","AOX3","ROUTINE","FALL_RISK","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","CARDIAC",
"URINAL",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","TRANSFER_TODAY",[], "", False, acuity_score=6, total_weighted_score=8)

patient5 = Patient("CVU","K0225","P5",2005,60,"F","2026-04-15","CONTACT","A","Dr",
"STEMI",[],[],"CABG",["CXR"],
"VT","BIPAP","AOX3","Q4H","FALL_RISK","ANXIOUS",
"IV_COMPLEX","Q1H","CONTINUOUS","CVAD","BEDREST","NPO",
"FOLEY",[], "COMPLEX_DRESSING","CONTROLLED","NONE","FAMILY","DAILY",
"NONE","NEW_ADMISSION",[], "", False, acuity_score=10, total_weighted_score=12)

patient6 = Patient("CVU","K0226","P6",2006,72,"M","2026-04-15","NONE","A","Dr",
"POST_CATH",[],[],"NONE",["CATH"],
"NSR","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","DM_CBGM",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","POSSIBLE_TRANSFER",[], "", False, acuity_score=5, total_weighted_score=7)

patient7 = Patient("CVU","K0230","P7",2007,68,"F","2026-04-15","NONE","A","Dr",
"CHF",[],[],"NONE",[],
"NSR","NP","AOX3","DAILY","NONE","COOPERATIVE",
"PO","DAILY","ROUTINE","NONE","ASSIST_X1","CARDIAC",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=4, total_weighted_score=6)

patient8 = Patient("CVU","K0255","P8",2008,75,"M","2026-04-15","NONE","A","Dr",
"POST_OP",[],[],"NONE",[],
"NSR","NP","AOX3","ROUTINE","FALL_RISK","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","CARDIAC",
"FOLEY",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","DISCHARGE_TODAY",[], "", False, acuity_score=5, total_weighted_score=7)

# -------- POD C --------
patient9 = Patient("CVU","K0231","P9",2009,76,"M","2026-04-15","NONE","A","Dr",
"CHF",[],[],"NONE",["TTE"],
"NSR","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","CARDIAC",
"TOILET",[], "NONE","CONTROLLED","NONE","FAMILY","DAILY",
"NONE","TRANSFER_TODAY",[], "", False, acuity_score=6, total_weighted_score=9)

patient10 = Patient("CVU","K0232","P10",2010,70,"F","2026-04-15","NONE","A","Dr",
"NSTEMI",[],[],"NONE",[],
"AFIB","NP","AOX3","ROUTINE","FALL_RISK","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","CARDIAC",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=5, total_weighted_score=7)

patient11 = Patient("CVU","K0240","P11",2011,85,"F","2026-04-15","NONE","C","Dr",
"CHF",[],[],"NONE",[],
"NSR","RA","AOX2","DAILY","NONE","CONFUSED",
"PO","DAILY","ROUTINE","NONE","ASSIST_X2","REGULAR",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=3, total_weighted_score=6)

patient12 = Patient("CVU","K0244","P12",2012,65,"M","2026-04-15","NONE","A","Dr",
"POST_CATH",[],[],"NONE",["CATH"],
"NSR","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","DM_CBGM",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","POSSIBLE_TRANSFER",[], "", False, acuity_score=5, total_weighted_score=7)

patient13 = Patient("CVU","K0250","P13",2013,72,"M","2026-04-15","NONE","A","Dr",
"ARRHYTHMIA",[],[],"NONE",[],
"AFIB","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","CARDIAC",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=5, total_weighted_score=7)

patient14 = Patient("CVU","K0251","P14",2014,68,"F","2026-04-15","NONE","A","Dr",
"CHF",[],[],"NONE",[],
"NSR","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"PO","DAILY","ROUTINE","NONE","ASSIST_X1","CARDIAC",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=4, total_weighted_score=6)

patient15 = Patient("CVU","K0254","P15",2015,69,"F","2026-04-15","NONE","A","Dr",
"POST_CATH",[],[],"NONE",["CATH"],
"NSR","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","DM_CBGM",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","STABLE",[], "", False, acuity_score=4, total_weighted_score=6)

patient16 = Patient("CVU","K0271","P16",2016,78,"M","2026-04-15","NONE","A","Dr",
"CHF",[],[],"NONE",[],
"NSR","NP","AOX3","ROUTINE","NONE","COOPERATIVE",
"IV_SIMPLE","ACHS","ENHANCED","PIV","SUPERVISION","CARDIAC",
"TOILET",[], "NONE","CONTROLLED","NONE","INDEP","DAILY",
"NONE","NEW_ADMISSION",[], "", False, acuity_score=7, total_weighted_score=9)


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