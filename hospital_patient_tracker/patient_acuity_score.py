# This is the clean scoring module structure  that is our scoring engine

# Acuity = How clinically heavy the patient is
# Workload = How much nursing time/ tasks they generate
# Modifiers = Special adjustments that are not pure acuity but still affect assignment fairness
"""
patient_acuity_score.py

Scoring engine for patient acuity and nursing workload.
Uses standardized fields from the Patient object.
"""

from report_standard import get_total_field_score, SPECIAL_FLAGS


# =========================================================
# 1. FIELD GROUPS
# =========================================================
# These decide WHICH category belongs to:
# - acuity
# - workload
# - modifiers

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

# Extra balancing factors for fair assignment
MODIFIER_FIELDS = [
    "isolation_status",
    "turnover",
    "behaviour_cooperation",
]


# =========================================================
# 2. FIELD WEIGHTS
# =========================================================
# These decide HOW IMPORTANT each field is.
# Default weight should be 1.0 if not listed.
#
# Example:
# raw field score = 2
# weight = 1.5
# weighted field score = 3.0

FIELD_WEIGHTS = {
    # -------- ACUITY --------
    "hemodynamic_status": 2.0,
    "cardiac_status": 1.5,
    "respiratory_status": 2.0,
    "neurological_status": 1.5,
    "lab_instability": 1.25,
    "safety_risk": 1.25,
    "medication_complexity": 1.5,
    "monitoring_frequency": 1.5,

    # -------- WORKLOAD --------
    "cbgm_frequency": 0.75,
    "iv_access": 1.0,
    "mobility": 1.5,
    "nutrition": 1.0,
    "elimination": 1.25,
    "procedures_tests": 1.25,
    "wounds_dressings": 1.5,
    "pain_management": 1.0,
    "communication": 0.75,
    "family_social": 0.75,
    "blood_test_frequency": 1.0,

    # -------- MODIFIERS --------
    "isolation_status": 1.0,
    "turnover": 1.5,
    "behaviour_cooperation": 1.5,
}


# =========================================================
# 3. HELPER FUNCTIONS
# =========================================================

# Safely fetches a field value from the patient object
def safe_get_patient_value(patient, field_name):
    """
    Safely get a field value from the patient object.
    Returns None if the attribute does not exist.
    """
    return getattr(patient, field_name, None)

# Gets the weight of the field. Example: hemodynamic_status is 2.0
def get_field_weight(field_name):
    """
    Return the weight for a field.
    If not found, default to 1.0.
    """
    return FIELD_WEIGHTS.get(field_name, 1.0)

 # Calculates all the raw total score of the fields
def calculate_fields_total(patient, field_list):
    """
    Calculate the RAW total score for a list of patient fields.
    Uses get_total_field_score() from report_standard.py.
    """
    total = 0

    for field_name in field_list:
        value = safe_get_patient_value(patient, field_name)

        if value is None:
            print(f"[WARNING] Field '{field_name}' not found in patient object.")
            continue

        total += get_total_field_score(field_name, value)

    return total


def calculate_weighted_fields_total(patient, field_list):
    """
    Calculate the WEIGHTED total score for a list of patient fields.
    """
    total = 0

    for field_name in field_list:
        value = safe_get_patient_value(patient, field_name)

        if value is None:
            print(f"[WARNING] Field '{field_name}' not found in patient object.")
            continue

        raw_score = get_total_field_score(field_name, value)
        weight = get_field_weight(field_name)
        weighted_score = raw_score * weight

        total += weighted_score

    return total


# =========================================================
# 4. MAIN RAW SCORE FUNCTIONS
# =========================================================

def calculate_acuity_raw(patient):
    """
    Calculate the raw clinical acuity score.
    """
    return calculate_fields_total(patient, ACUITY_FIELDS)


def calculate_workload_raw(patient):
    """
    Calculate the raw nursing workload score.
    """
    return calculate_fields_total(patient, WORKLOAD_FIELDS)


def calculate_modifiers_raw(patient):
    """
    Calculate the raw modifier score.
    Includes:
    - modifier fields
    - optional special_flags
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
# 5. MAIN WEIGHTED SCORE FUNCTIONS
# =========================================================

def calculate_acuity_weighted(patient):
    """
    Calculate the weighted clinical acuity score.
    """
    return calculate_weighted_fields_total(patient, ACUITY_FIELDS)


def calculate_workload_weighted(patient):
    """
    Calculate the weighted nursing workload score.
    """
    return calculate_weighted_fields_total(patient, WORKLOAD_FIELDS)


def calculate_modifiers_weighted(patient):
    """
    Calculate the weighted modifier score.
    Special flags are added as-is for now.
    """
    total = calculate_weighted_fields_total(patient, MODIFIER_FIELDS)

    special_flags = safe_get_patient_value(patient, "special_flags")

    if special_flags is None:
        special_flags = []

    for flag in special_flags:
        cleaned_flag = str(flag).strip().upper()
        total += SPECIAL_FLAGS.get(cleaned_flag, 0)

    return total


# =========================================================
# 6. FINAL SUMMARY FUNCTIONS
# =========================================================

# Getting the patient_assignment_score but not printing
def get_patient_assignment_score(patient):
    """
    Return both raw and weighted score breakdown.

    Returns a dictionary with:
    - raw acuity / workload / modifier / total
    - weighted acuity / workload / modifier / total
    """
    acuity_raw = calculate_acuity_raw(patient)
    workload_raw = calculate_workload_raw(patient)
    modifiers_raw = calculate_modifiers_raw(patient)

    total_raw = acuity_raw + workload_raw + modifiers_raw

    acuity_weighted = calculate_acuity_weighted(patient)
    workload_weighted = calculate_workload_weighted(patient)
    modifiers_weighted = calculate_modifiers_weighted(patient)

    total_weighted = acuity_weighted + workload_weighted + modifiers_weighted

    return {
        "acuity_raw": acuity_raw,
        "workload_raw": workload_raw,
        "modifiers_raw": modifiers_raw,
        "total_raw": total_raw,

        "acuity_weighted": round(acuity_weighted, 2),
        "workload_weighted": round(workload_weighted, 2),
        "modifiers_weighted": round(modifiers_weighted, 2),
        "total_weighted": round(total_weighted, 2),
    }

#Printing the score breakdown using get_patient_assignment_score
def print_score_breakdown(patient):
    """
    Print a simple summary of raw and weighted scores.
    """
    scores = get_patient_assignment_score(patient)

    print("\n--- PATIENT SCORE SUMMARY ---")
    print(f"Raw Acuity Score:       {scores['acuity_raw']}")
    print(f"Raw Workload Score:     {scores['workload_raw']}")
    print(f"Raw Modifier Score:     {scores['modifiers_raw']}")
    print(f"Raw Total Score:        {scores['total_raw']}")

    print()

    print(f"Weighted Acuity Score:  {scores['acuity_weighted']}")
    print(f"Weighted Workload Score: {scores['workload_weighted']}")
    print(f"Weighted Modifier Score: {scores['modifiers_weighted']}")
    print(f"Weighted Total Score:   {scores['total_weighted']}")


# =========================================================
# 7. DETAILED BREAKDOWN
# =========================================================

#Getting the detailed_score_breakdown to understand where the point are allocated
def get_detailed_score_breakdown(patient):
    """
    Return a detailed breakdown for each field:
    - value
    - raw score
    - weight
    - weighted score
    """
    breakdown = {
        "acuity": {},
        "workload": {},
        "modifiers": {},
        "special_flags": {},
    }

    # Acuity
    for field_name in ACUITY_FIELDS:
        value = safe_get_patient_value(patient, field_name)

        if value is None:
            continue

        raw_score = get_total_field_score(field_name, value)
        weight = get_field_weight(field_name)
        weighted_score = raw_score * weight

        breakdown["acuity"][field_name] = {
            "value": value,
            "raw_score": raw_score,
            "weight": weight,
            "weighted_score": round(weighted_score, 2),
        }

    # Workload
    for field_name in WORKLOAD_FIELDS:
        value = safe_get_patient_value(patient, field_name)

        if value is None:
            continue

        raw_score = get_total_field_score(field_name, value)
        weight = get_field_weight(field_name)
        weighted_score = raw_score * weight

        breakdown["workload"][field_name] = {
            "value": value,
            "raw_score": raw_score,
            "weight": weight,
            "weighted_score": round(weighted_score, 2),
        }

    # Modifiers
    for field_name in MODIFIER_FIELDS:
        value = safe_get_patient_value(patient, field_name)

        if value is None:
            continue

        raw_score = get_total_field_score(field_name, value)
        weight = get_field_weight(field_name)
        weighted_score = raw_score * weight

        breakdown["modifiers"][field_name] = {
            "value": value,
            "raw_score": raw_score,
            "weight": weight,
            "weighted_score": round(weighted_score, 2),
        }

    # Special flags
    special_flags = safe_get_patient_value(patient, "special_flags")
    if special_flags is None:
        special_flags = []

    for flag in special_flags:
        cleaned_flag = str(flag).strip().upper()
        breakdown["special_flags"][cleaned_flag] = SPECIAL_FLAGS.get(cleaned_flag, 0)

    return breakdown

# Printing the full details for the patient score breakdown using breakdown and 
def print_detailed_score_breakdown(patient):
    """
    Print a detailed breakdown field by field.
    """
    breakdown = get_detailed_score_breakdown(patient)
    totals = get_patient_assignment_score(patient)

    print("\n========== DETAILED PATIENT SCORE BREAKDOWN ==========")

    print("\n--- ACUITY ---")
    for field, info in breakdown["acuity"].items():
        print(
            f"{field}: {info['value']} "
            f"-> raw={info['raw_score']}, weight={info['weight']}, weighted={info['weighted_score']}"
        )

    print("\n--- WORKLOAD ---")
    for field, info in breakdown["workload"].items():
        print(
            f"{field}: {info['value']} "
            f"-> raw={info['raw_score']}, weight={info['weight']}, weighted={info['weighted_score']}"
        )

    print("\n--- MODIFIERS ---")
    for field, info in breakdown["modifiers"].items():
        print(
            f"{field}: {info['value']} "
            f"-> raw={info['raw_score']}, weight={info['weight']}, weighted={info['weighted_score']}"
        )

    print("\n--- SPECIAL FLAGS ---")
    if breakdown["special_flags"]:
        for flag, score in breakdown["special_flags"].items():
            print(f"{flag} -> {score}")
    else:
        print("None")

    print("\n--- TOTALS ---")
    print(f"Raw Acuity Score:        {totals['acuity_raw']}")
    print(f"Raw Workload Score:      {totals['workload_raw']}")
    print(f"Raw Modifier Score:      {totals['modifiers_raw']}")
    print(f"Raw Total Score:         {totals['total_raw']}")
    print()
    print(f"Weighted Acuity Score:   {totals['acuity_weighted']}")
    print(f"Weighted Workload Score: {totals['workload_weighted']}")
    print(f"Weighted Modifier Score: {totals['modifiers_weighted']}")
    print(f"Weighted Total Score:    {totals['total_weighted']}")


# =========================================================
# 8. MINI TEST
# =========================================================
# This lets you test the file by itself.

if __name__ == "__main__":

    class MockPatient:
        def __init__(self):
            # ---- Acuity ----
            self.hemodynamic_status = "STABLE"
            self.cardiac_status = "AFIB"
            self.respiratory_status = "NP"
            self.neurological_status = "AOX3"
            self.lab_instability = "ROUTINE"
            self.safety_risk = "FALL_RISK"
            self.medication_complexity = "IV_SIMPLE"
            self.monitoring_frequency = "ENHANCED"

            # ---- Workload ----
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

            # ---- Modifiers ----
            self.isolation_status = "CONTACT"
            self.turnover = "POSSIBLE_TRANSFER"
            self.behaviour_cooperation = "ANXIOUS"

            # ---- Optional extra flags ----
            self.special_flags = ["FREQUENT_CALLER"]

    patient = MockPatient()


    print("\n--- TESTING HELPER: safe_get_patient_value() ---")
    print(safe_get_patient_value(patient, "hemodynamic_status"))   # expected: STABLE
    print(safe_get_patient_value(patient, "mobility"))             # expected: SUPERVISION
    print(safe_get_patient_value(patient, "fake_field"))           # expected: None

    print("\n--- TESTING HELPER: get_field_weight() ---")
    print(get_field_weight("hemodynamic_status"))                  # expected: 2.0
    print(get_field_weight("mobility"))                            # expected: 1.5
    print(get_field_weight("fake_field"))                          # expected: 1.0

    print("\n--- TESTING HELPER: calculate_fields_total() ---")
    print(calculate_fields_total(patient, ["hemodynamic_status", "cardiac_status"]))  # expected raw score of STABLE = 0 + AFIB = 2
    print(calculate_fields_total(patient, ["cardiac_status"]))      # expected raw score of AFIB = 2
    print(calculate_fields_total(patient, ["procedures_tests"]))    # expected raw score of ['CXR', 'TTE'] = 2
    print(calculate_fields_total(patient, ["mobility", "nutrition", "elimination"]))

    print("\n--- TESTING HELPER: calculate_weighted_fields_total() ---")
    print(calculate_weighted_fields_total(patient, ["hemodynamic_status", "cardiac_status"]))  # (0 * 2.0 = 0)  + (2 *1.5 = 3 ) = 3
    print(calculate_weighted_fields_total(patient, ["cardiac_status"]))      # 2 * 1.5 = 3.0
    print(calculate_weighted_fields_total(patient, ["mobility"]))            # 1 * 1.5 = 1.5
    print(calculate_weighted_fields_total(patient, ["procedures_tests"]))    # 2 * 1.25 = 2.5

    print("\n--- TESTING MAIN RAW FUNCTIONS ---")
    print("Acuity raw:", calculate_acuity_raw(patient))
    print("Workload raw:", calculate_workload_raw(patient))
    print("Modifiers raw:", calculate_modifiers_raw(patient))

    print("\n--- TESTING MAIN WEIGHTED FUNCTIONS ---")
    print("Acuity weighted:", calculate_acuity_weighted(patient))
    print("Workload weighted:", calculate_workload_weighted(patient))
    print("Modifiers weighted:", calculate_modifiers_weighted(patient))

    print("\n--- TESTING FINAL SUMMARY FUNCTION ---")
    print(get_patient_assignment_score(patient))


    print_score_breakdown(patient)
    print_detailed_score_breakdown(patient)