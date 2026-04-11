#report_standards.py is a file so that I have standardized values in the report

# Fix this for NON_SCORING FIELDS
NON_SCORING__FIELDS = {
    
    "level_of_intervention": {
        "A", "B", "C", "D"
    },

    "diagnosis" : {
        "NSTEMI", "STEMI", "ACS", "AS", "CHF", "CHFE" "SYNCOPE", "FAF", "BVHF", "PNA", "UTI", "E.CABG", "CABG", "ADHF", "PH"
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
SCORING__FIELDS = {

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
        3: {"TITRATABLE_DRIP", "VASOPRESSOR", "SEDATION_DRIP", "ANTIARRHYTHMIC_DRIP"},
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
            "POST_PACEMAKER", "CARDIOVERSION", "PRE_PCI", "TEMP_PACER_INSERTION"
        },
        4: {"PRE_CABG", "PRE_TAVI", "FRESH_POST_OP"},
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


#CONSIDER ADDING MODIFIERS


#Transforms all value in upper case
def normalize_term(value):
    return value.strip().upper()

# Validates if the field exists actually and then normalizes the term 
def validate_single_value(field_name, value):
    if field_name not in STANDARD_FIELDS:
        return True, value   # unspecified/free-text fields allowed

    normalized = normalize_term(value)

    if normalized in STANDARD_FIELDS[field_name]:
        return True, normalized

    return False, None

#Validates the fields with multiple values
def validate_multi_value(field_name, value):
    if field_name not in STANDARD_FIELDS:
        return True, value

    items = [normalize_term(item) for item in value.split(",") if item.strip()]
    invalid_items = []

    for item in items:
        if item not in STANDARD_FIELDS[field_name]:
            invalid_items.append(item)

    if invalid_items:
        return False, invalid_items

    return True, items

def get_allowed_values(field_name):
    if field_name in STANDARD_FIELDS:
        return sorted(STANDARD_FIELDS[field_name])
    return []