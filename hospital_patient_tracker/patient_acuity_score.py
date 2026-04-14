# This is the clean scoring module structure  that is our scoring engine

# Acuity = How clinically heavy the patient is
# Workload = How much nursing time/ tasks they generate
# Modifiers = Special adjustments that are not pure acuity but still affect assignment fairness

"""
Scoring engine for patient acuity and nursing workload.
Uses standardized fields from the Patient Object
"""

from report_standard import get_total_field_score, SPECIAL_FLAGS

#--------------------------------------
#1. FIELD GROUPS
#--------------------------------------

#Clinical severity / instability

# Clinical severity / instability
ACUITY_FIELDS = [
    "hemodynamic_status",
    "cardiac_status",
    "respiratory_status",
    "neurological_status",
    "lab_instability",
    "safety_risk",
    "medication_complexity",
    "monitoring_frequency",
]

# Nursing task burden / time demand
WORKLOAD_FIELDS = [
    "cbgm_frequency",
    "iv_access",
    "mobility",
    "nutrition",
    "elimination",
    "procedures_tests",
    "wounds_dressings",
    "pain_management",
    "communication",
    "family_social",
    "blood_test_frequency",
]

# Extra balancing factors for assignment fairness
MODIFIER_FIELDS = [
    "isolation_status",
    "turnover",
    "behaviour_cooperation",
]

# =========================================================
# 2. HELPER FUNCTIONS
# =========================================================

def safe_get_patient_value(patient, field_name):
    """
    Safely get a field value from the Patient object.
    Returns None if the attribute does not exist.
    """
    return getattr(patient, field_name, None)


def calculate_fields_total(patient, field_list):
    """
    Calculate the total score for a list of patient fields.
    Uses report_standard.get_total_field_score().
    """
    total = 0

    for field_name in field_list:
        value = safe_get_patient_value(patient, field_name)

        if value is None:
            continue

        total += get_total_field_score(field_name, value)

    return total

# =========================================================
# 3. MAIN SCORING SECTIONS
# =========================================================

def calculate_acuity(patient):
    """
    Calculate the base clinical acuity score.
    """
    return calculate_fields_total(patient, ACUITY_FIELDS)


def calculate_workload(patient):
    """
    Calculate the nursing workload score.
    """
    return calculate_fields_total(patient, WORKLOAD_FIELDS)


def calculate_modifiers(patient):
    """
    Calculate extra assignment modifiers.
    
    Includes:
    - modifier fields from the patient object
    - optional special_flags list on the patient object
    """
    total = calculate_fields_total(patient, MODIFIER_FIELDS)

    special_flags = safe_get_patient_value(patient, "special_flags")

    if special_flags is None:
        special_flags = []

    for flag in special_flags:
        cleaned_flag = str(flag).strip().upper()
        total += SPECIAL_FLAGS.get(cleaned_flag, 0)

    return total


# =========================================================
# 4. FINAL SCORE SUMMARY
# =========================================================

def get_patient_assignment_score(patient):
    """
    Return a full breakdown of patient scoring.

    Returns a dictionary with:
    - acuity_score
    - workload_score
    - modifier_score
    - total_score
    """
    acuity_score = calculate_acuity(patient)
    workload_score = calculate_workload(patient)
    modifier_score = calculate_modifiers(patient)

    total_score = acuity_score + workload_score + modifier_score

    return {
        "acuity_score": acuity_score,
        "workload_score": workload_score,
        "modifier_score": modifier_score,
        "total_score": total_score,
    }


def print_score_breakdown(patient):
    """
    Print a clean score breakdown for one patient.
    """
    scores = get_patient_assignment_score(patient)

    print("\n--- PATIENT ACUITY / WORKLOAD SCORE ---")
    print(f"Acuity Score:   {scores['acuity_score']}")
    print(f"Workload Score: {scores['workload_score']}")
    print(f"Modifier Score: {scores['modifier_score']}")
    print(f"Total Score:    {scores['total_score']}")


# =========================================================
# 5. OPTIONAL DETAILED BREAKDOWN
# =========================================================

def get_detailed_score_breakdown(patient):
    """
    Return a detailed breakdown showing each field's contribution.
    Useful for debugging and refining your scoring model.
    """
    breakdown = {
        "acuity": {},
        "workload": {},
        "modifiers": {},
        "special_flags": {},
    }

    # Acuity fields
    for field_name in ACUITY_FIELDS:
        value = safe_get_patient_value(patient, field_name)
        if value is not None:
            breakdown["acuity"][field_name] = {
                "value": value,
                "score": get_total_field_score(field_name, value)
            }

    # Workload fields
    for field_name in WORKLOAD_FIELDS:
        value = safe_get_patient_value(patient, field_name)
        if value is not None:
            breakdown["workload"][field_name] = {
                "value": value,
                "score": get_total_field_score(field_name, value)
            }

    # Modifier fields
    for field_name in MODIFIER_FIELDS:
        value = safe_get_patient_value(patient, field_name)
        if value is not None:
            breakdown["modifiers"][field_name] = {
                "value": value,
                "score": get_total_field_score(field_name, value)
            }

    # Special flags
    special_flags = safe_get_patient_value(patient, "special_flags")
    if special_flags is None:
        special_flags = []

    for flag in special_flags:
        cleaned_flag = str(flag).strip().upper()
        breakdown["special_flags"][cleaned_flag] = SPECIAL_FLAGS.get(cleaned_flag, 0)

    return breakdown


def print_detailed_score_breakdown(patient):
    """
    Print a detailed score breakdown field by field.
    """
    breakdown = get_detailed_score_breakdown(patient)
    totals = get_patient_assignment_score(patient)

    print("\n========== DETAILED PATIENT SCORE BREAKDOWN ==========")

    print("\n--- ACUITY ---")
    for field, info in breakdown["acuity"].items():
        print(f"{field}: {info['value']} -> {info['score']}")

    print("\n--- WORKLOAD ---")
    for field, info in breakdown["workload"].items():
        print(f"{field}: {info['value']} -> {info['score']}")

    print("\n--- MODIFIERS ---")
    for field, info in breakdown["modifiers"].items():
        print(f"{field}: {info['value']} -> {info['score']}")

    print("\n--- SPECIAL FLAGS ---")
    if breakdown["special_flags"]:
        for flag, score in breakdown["special_flags"].items():
            print(f"{flag} -> {score}")
    else:
        print("None")

    print("\n--- TOTALS ---")
    print(f"Acuity Score:   {totals['acuity_score']}")
    print(f"Workload Score: {totals['workload_score']}")
    print(f"Modifier Score: {totals['modifier_score']}")
    print(f"Total Score:    {totals['total_score']}")


# =========================================================
# 6. MINI TEST
# =========================================================

if __name__ == "__main__":
    class MockPatient:
        def __init__(self):
            self.hemodynamic_status = "STABLE"
            self.cardiac_status = "AFIB"
            self.respiratory_status = "NP"
            self.neurological_status = "AOX3"
            self.lab_instability = "ROUTINE"
            self.safety_risk = "FALL_RISK"
            self.medication_complexity = "IV_SIMPLE"
            self.monitoring_frequency = "ENHANCED"

            self.cbgm_frequency = "ACHS"
            self.iv_access = "PIV"
            self.mobility = "SUPERVISION"
            self.nutrition = "DM_CBGM"
            self.elimination = "FOLEY"
            self.procedures_tests = ["CXR", "TTE"]
            self.wounds_dressings = "NONE"
            self.pain_management = "CONTROLLED"
            self.communication = "NONE"
            self.family_social = "INDEP"
            self.blood_test_frequency = "DAILY"

            self.isolation_status = "CONTACT"
            self.turnover = "POSSIBLE_TRANSFER"
            self.behaviour_cooperation = "ANXIOUS"

            self.special_flags = ["FREQUENT_CALLER"]

    patient = MockPatient()

    print_score_breakdown(patient)
    print_detailed_score_breakdown(patient)
