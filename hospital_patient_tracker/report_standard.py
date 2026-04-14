#report_standards.py is a file so that I have standardized values in the report

# Fields that are standardized but do not directly score
NON_SCORING_FIELDS = {
    
    "level_of_intervention": {
        "A", "B", "C", "D"
    },

    "diagnosis" : {
        "NSTEMI", "STEMI", "ACS", "AS", "CHF", "CHFE", "SYNCOPE", "FAF", "BVHF", "PNA", "UTI", "E_CABG", "CABG", "ADHF", "PH"
    },

    "pmhx": {
        # --- Cardiac ---
        "CAD", "CHF", "AFIB", "VALVE_DZ", "CARDIOMYOPATHY", "MI",

        # --- Respiratory ---
        "COPD", "ASTHMA", "OSA",

        # --- Renal ---
        "CKD", "ESRD",

        # --- Endocrine ---
        "DM2", "DM1", "HYPOTHYROID", "HYPERTHYROID",

        # --- Neuro ---
        "CVA", "TIA", "DEMENTIA", "PARKINSONS", "SEIZURE_DX",

        # --- Vascular ---
        "HTN", "DLP", "HLP", "PAD", "DVT", "PE",

        # --- GI / Liver ---
        "GERD", "LIVER_DZ", "CIRRHOSIS", "GI_BLEED",

        # --- Hematology / Oncology ---
        "CANCER", "ANEMIA", "COAGULOPATHY",

        # --- Pulmonary vascular ---
        "PH",

        # --- Infectious / Immune ---
        "HIV", "IMMUNOSUPPRESSED", "TRANSPLANT",

        # --- MSK / Frailty ---
        "OP", "ARTHRITIS", "FRAILTY",

        # --- Social ---
        "SMOKER", "ETOH", "SUBSTANCE_USE"
    },

    "pro_involved":{
        "PT", "OT", "SW", "CARDIO", "NEPHRO", "DERM", "THROMBO", "NEURO", "URO", "ID", "GERI", 
        "DIET", "PULM", "RHEUM", "HEME", "DCPN", 
    },

}


#SCORING FIELDS----------------------------------------------------------------------
#Fields that contribute to acuity / workload scoring
SCORING_FIELDS = {

    "hemodynamic_status": {
        0: {"STABLE"},
        1: {"SOFT_BP"},
        2: {"SINGLE_PRESSOR"},
        3: {"TITRATING_PRESSORS"},
        4: {"MULTIPLE_PRESSORS", "ACTIVE_BLEED", "MECH_SUPPORT"},
    },

    "cardiac_status": {
        0: {"NSR", "NONE"},
        1: {"SB", "ST", "PAC", "PVC", "1AVB"},
        2: {"AFLUTTER", "AFIB", "SVT", "JUNCTIONAL", "2AVB1", "NSVT"},
        3: {"2AVB2", "3AVB", "CHB_PACED", "VT"},
        4: {"VFIB", "ASYSTOLE"},
    },


    "respiratory_status": {
        0: {"RA", "NP", "NC"},
        2: {"CPAP", "BIPAP", "TRACH_MASK"},
        4: {"VENTED"},
    },


    "neurological_status": {
        0: {"AOX3"},
        1: {"AOX2", "CONFUSED"},
        2: {"AOX1", "DELIRIUM", "AGITATED"},
        3: {"LETHARGIC", "SEDATED", "OBTUNDED"},
        4: {"UNRESPONSIVE"},
    },


    "lab_instability": {
        0: {"ROUTINE"},
        1: {
            "K_ABNORMAL", "NA_ABNORMAL", "MG_ABNORMAL", "CA_ABNORMAL",
            "HGB_LOW", "PLT_LOW", "CREATININE_ABNORMAL", "WBC_ABNORMAL", "INR_ABNORMAL"
        },
        2: {"REPEAT_LABS", "FREQUENT_LABS"},
        3: {"ABG_MONITORING", "LACTATE_ELEVATED", "CRITICAL_LABS"},
        4: {"CONTINUOUS_CORRECTION"},
    },


    "safety_risk": {
        0: {"NONE"},
        1: {"FALL_RISK"},
        2: {"HIGH_FALL_RISK", "IMPULSIVE"},
        3: {"WANDERING", "PULLING_LINES", "CONFUSED_UNSAFE"},
        4: {"RESTRAINTS", "SITTER", "VIOLENT"},
    },


    "behaviour_cooperation": {
        0: {"COOPERATIVE"},
        1: {"ANXIOUS"},
        2: {"DEMANDING"},
        3: {"DISRUPTIVE"},
        4: {"AGGRESSIVE"},
    },

    "medication_complexity": {
        0: {"PO_ONLY"},
        1: {"IV_SIMPLE"},
        2: {"IV_MULTIPLE", "INSULIN_INFUSION"},
        3: {"TITRATABLE_DRIP", "VASOPRESSOR", "SEDATION_DRIP", "ANTIARRHYTHMIC_DRIP", "CHEMO"},
        4: {"MULTIPLE_TITRATABLE_DRIPS"},
    },


    "cbgm_frequency": {
        0: {"NONE"},
        1: {"ACHS"},
        4: {"Q1H"},
    },


    "monitoring_frequency": {
        0: {"ROUTINE"},
        1: {"ENHANCED"},
        2: {"Q2H"},
        3: {"Q1H"},
        4: {"CONTINUOUS"},
    },


    "iv_access": {
        0: {"NONE"},
        1: {"PIV", "MIDLINE"},
        2: {"PICC", "CVAD"},
        3: {"ARTLINE", "PA_LINE", "HD_LINE"},
    },


    "mobility": {
        0: {"INDEP", "AMB"},
        1: {"SUPERVISION", "CANE", "WALKER"},
        2: {"AX1", "WC", "BEDBOUND"},
        3: {"AX2", "BRODA"},
        4: {"TOTAL_CARE", "LIFT"},
    },


    "nutrition": {
        0: {"REGULAR", "CARDIAC", "DM_NO_CBGM"},
        1: {"DM_CBGM", "FR1L", "FR1_5L", "FR2L", "SETUP", "NPO"},
        2: {"FEED_ASSIST", "ASP_PRECAUTIONS"},
        3: {"NGT_FEEDS", "OGT_FEEDS", "PEG_FEEDS"},
        4: {"TPN"},
    },


    "elimination": {
        0: {"NONE", "TOILET", "COMMODE", "URINAL"},
        1: {"FOLEY", "DIAPER"},
        2: {"INCONTINENT", "DIARRHEA"},
        3: {"HIGH_OUTPUT_STOOL", "SKIN_BREAKDOWN_RISK", "BOWEL_CARE", "COLOSTOMY"},
    },

    "procedures_tests": {
        0: {"NONE"},
        1: {"CXR", "TTE", "CT", "MRI"},
        2: {"TEE", "HEMODIALYSIS", "BRONCHOSCOPY", "THORACENTESIS", "LINE_INSERTION"},
        3: {
            "PRE_ANGIOGRAPHY", "PRE_PACEMAKER", "POST_ANGIOGRAPHY",
            "POST_PACEMAKER", "CARDIOVERSION", "PRE_PCI", "TEMP_PACER_INSERTION",
        },
        4: {"PRE_CABG", "PRE_TAVI", "FRESH_POST_OP", "CRRT"},
    },


    "wounds_dressings": {
        0: {"NONE"},
        1: {"SIMPLE_DRESSING", "SKIN_TEARS"},
        2: {"STERNAL_DRESSING", "MULTIPLE_DRESSINGS", "DIFFICULT_DRESSINGS"},
        3: {"TRACH_CARE", "CHEST_TUBE_CARE", "DRAIN_CARE", "PPM_DRESSING"},
        4: {"VAC_DRESSING", "COMPLEX_WOUND", "MULTIPLE_COMPLEX_WOUNDS", "BLEEDING_WOUND", "INFECTED_WOUND"},
    },


    "pain_management": {
        0: {"CONTROLLED"},
        1: {"PRN_OCCASIONAL"},
        2: {"PRN_FREQUENT"},
        3: {"PCA"},
        4: {"UNCONTROLLED"},
    },


    "communication": {
        0: {"NONE"},
        1: {"MILD"},
        2: {"BARRIER"},
        3: {"FAMILY_REQUIRED"},
        4: {"SEVERE"},
    },


    "family_social": {
        0: {"INDEP"},
        1: {"EDUCATION"},
        2: {"SUPPORT"},
        3: {"COMPLEX"},
        4: {"EXTREME"},
    },


    "blood_test_frequency": {
        0: {"DAILY"},
        1: {"ONE_REPEAT"},
        2: {"Q12H", "Q8H"},
        3: {"Q6H", "Q4H"},
        4: {"Q2H", "Q1H", "URGENT_REPEAT"},
    },


    "isolation_status": {
        0: {"NONE"},
        1: {"CONTACT", "LRC", "MRSA", "VRE", "MDRO", "CRO", "BEDBUGS", "SCABIES"},
        2: {"MRC", "HRC", "CDIFF", "CDIFF_R_O", "DROPLET", "COVID", "R_O_COVID"},
        3: {"TB_R_O", "AIRBORNE"},
    },

    "turnover": {
        0: {"STABLE"},
        1: {"POSSIBLE_TRANSFER"},
        2: {"TRANSFER_TODAY", "DISCHARGE_TODAY"},
        3: {"NEW_ADMISSION", "TRANSFER_TO_FLOOR"},
        4: {"MULTIPLE_TURNOVER"},
    },
}

#_________________________________________________________

# Optional additive modifiers

SPECIAL_FLAGS = {
    "BLOOD_TRANSFUSION": 2,
    "FREQUENT_CALLER": 1,
    "ONE_TO_ONE_OBSERVATION": 2,
    "BARIATRIC_HEAVY_CARE": 1,
    "END_OF_LIFE_COMFORT" : 1,
    "POST_OP_FRESH_ARRIVAL": 2
}


MULTI_VALUE_SCORING_FIELDS = {
    "procedures_tests",
    "wounds_dressings"
}

FIELD_SCORING_RULES = {
    "procedures_tests": "sum_cap_4",
    "wounds_dressings": "sum_cap_4"
}

# =========================================================
# BUILD MASTER STANDARD_FIELDS AUTOMATICALLY
# =========================================================

def build_standard_fields():
    standard_fields = {}

    # Flatten scoring fields into standard validation fields
    for field_name, score_map in SCORING_FIELDS.items():   #hemodynamic_status, 0
        allowed_values = set()

        for values in score_map.values():  #"STABLE"
            allowed_values.update(values)

        standard_fields[field_name] = allowed_values

    # Add non-scoring fields
    for field_name, allowed_values in NON_SCORING_FIELDS.items():
        standard_fields[field_name] = set(allowed_values)

    return standard_fields


STANDARD_FIELDS = build_standard_fields()

#print(STANDARD_FIELDS)

# =========================================================
# 5. HELPER FUNCTIONS
# =========================================================

def is_valid_field(field_name):
    """Return True if the field exists in the standardized system."""
    return field_name in STANDARD_FIELDS

print(is_valid_field ("hemodynamic_status"))

def is_valid_value(field_name, value):
    """Return True if value is valid for the given field."""
    if field_name not in STANDARD_FIELDS:
        return False
    return value in STANDARD_FIELDS[field_name]

print(is_valid_value("hemodynamic_status", "STABLE"))

def validate_single_value(field_name, value):
    """
    Validate a single-value field.
    Returns: (True, cleaned_value) or (False, error_message)
    """
    if not is_valid_field(field_name):
        return False, f"Invalid field: {field_name}"

    cleaned_value = value.strip().upper()

    if not is_valid_value(field_name, cleaned_value):
        return False, f"Invalid value '{value}' for field '{field_name}'"

    return True, cleaned_value

print(validate_single_value("hemodynamic_status", "STABLE"))

# ["CKD", "DM2", "CAD"] Is this valid? Needed for Multi aspects inside the field 
def validate_multi_value(field_name, values):
    """
    Validate a list of values for fields like pmhx or pro_involved.
    Returns: (True, cleaned_values_list) or (False, error_message)
    """
    if not is_valid_field(field_name):
        return False, f"Invalid field: {field_name}"

    cleaned_values = []
    invalid_values = []

    for value in values:
        cleaned_value = value.strip().upper()
        if is_valid_value(field_name, cleaned_value):
            cleaned_values.append(cleaned_value)
        else:
            invalid_values.append(value)

    if invalid_values:
        return False, f"Invalid values for '{field_name}': {', '.join(invalid_values)}"

    return True, cleaned_values


def get_score(field_name, value):
    """
    Return the acuity/workload score for a valid scoring field value.
    Non-scoring fields return 0.
    """
    if field_name not in SCORING_FIELDS:
        return 0

    cleaned_value = value.strip().upper()

    for score, values in SCORING_FIELDS[field_name].items():
        if cleaned_value in values:
            return score

    return 0

print(get_score("hemodynamic_status", "STABLE"))

def get_allowed_values(field_name):
    """Return sorted allowed values for a field."""
    if field_name not in STANDARD_FIELDS:
        return []
    return sorted(STANDARD_FIELDS[field_name])

print(get_allowed_values("hemodynamic_status"))

def get_all_field_names():
    """Return all standardized field names."""
    return sorted(STANDARD_FIELDS.keys())

#print(get_all_field_names())

#Helper function that allows to check sum_cap_4
def get_total_field_score(field_name, value):
    if field_name not in SCORING_FIELDS:
        return 0

    if field_name in MULTI_VALUE_SCORING_FIELDS:
        if not isinstance(value, list):
            value = [value]

        scores = [get_score(field_name, item) for item in value]

        rule = FIELD_SCORING_RULES.get(field_name, "sum")

        if rule == "sum_cap_4":
            return min(sum(scores), 4)

        return sum(scores)

    return get_score(field_name, value)

#---------------------------
#print("\n--- SPECIAL FLAGS TEST ---")

#print(SPECIAL_FLAGS.get("BLOOD_TRANSFUSION", 0))  # 1
#print(SPECIAL_FLAGS.get("FREQUENT_CALLER", 0))    # 1
#print(SPECIAL_FLAGS.get("UNKNOWN_FLAG", 0))       # 0

#_________________________________________________________

#Here is a mini report simulation 

print("\n--- MINI REPORT SIMULATION ---")

patient_report = {
    "level_of_intervention": "A",
    "diagnosis": "nstemi",
    "pmhx": ["HYPOTHYROID", "DM2", "OP"],
    "hemodynamic_status": "stable",
    "cardiac_status" : "afib",
    "respiratory_status" : "NP",
    "neurological_status" : "AOX3",
    "lab_instability": "ROUTINE",
    "safety_risk" : "FALL_RISK",
    "behaviour_cooperation": "ANXIOUS",
    "medication_complexity": "IV_SIMPLE",
    "cbgm_frequency": "ACHS",
    "monitoring_frequency": "ENHANCED",
    "iv_access": "PIV",
    "mobility": "SUPERVISION",
    "nutrition": "DM_CBGM",
    "elimination": "FOLEY",
    "procedures_tests" : ["CXR", "TTE"],
    "wounds_dressings" : "NONE",
    "pain_management" : "CONTROLLED",
    "communication" : "NONE",
    "family_social" : "INDEP",
    "blood_test_frequency": "DAILY",
    "isolation_status": "CONTACT",
    "turnover": "POSSIBLE_TRANSFER",
    "pro_involved": ["PT", "OT", "SW"]
}

total_score = 0

for field, value in patient_report.items():
    if isinstance(value, list):
        valid, cleaned = validate_multi_value(field, value)
    else:
        valid, cleaned = validate_single_value(field, value)

    print(field, "->", valid, cleaned)

    if valid:
        total_score += get_total_field_score(field, cleaned)

print("Total score:", total_score)