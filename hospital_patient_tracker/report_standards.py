#report_standards.py is a file so that I have standardized values in the report


STANDARD_FIELDS = {
    "isolation": {
        "NONE",
        "CONTACT", "LRC", "MRC", "HRC",
        "MRSA", "VRE", "MDRO", "CRO",
        "CDIFF", "CDIFF_R_O",
        "BEDBUGS", "SCABIES",
        "DROPLET", "COVID", "R_O_COVID",
        "TB_R_O", "AIRBORNE"
    },

    "level_of_intervention": {
        "A", "B", "C", "D"
    },

    "diagnosis": {
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

    "neuro": { "AOX3", "AOX2", "AOX1", "CONFUSED", "DELIRIUM", "AGITATED", "LETHARGIC", "OBTUNDED", "SEDATED", "UNRESPONSIVE"
    },

    "procedure": {
        "NONE", "CXR", "TTE", "XRAY", "CT", "MRI",
        "TEE", "HEMODIALYSIS", "BRONCHOSCOPY","THORACENTESIS", "LINE_INSERTION",
        "PRE_ANGIOGRAPHY", "PRE_PACEMAKER", "POST_ANGIOGRAPHY", "POST_PACEMAKER", "CARDIOVERSION", "PCI", "TEMP_PACER_INSERTION",
        "CABG_1ST_CASE", "CABG_2ND_CASE", "TAVI_1ST_CASE", "TAVI_2ND_CASE", "TAVI_3RD_CASE",
        "FRESH_POST_OP"
        },
    "rhythm": {
        "NSR", "SB", "ST", "AFLUTTER", "AFIB", "JUNCTIONAL",
        "1AVB", "2AVB1", "2AVB2", "3AVB",
        "NSVT", "VT", "VFIB", "PAC", "PVC", "NONE",
        "SVT", "V_PACED", "A_PACED", "AV_PACED" ,"CHB_PACED", "ASYSTOLE" 
    },

    "ventilation": {
        "RA", "NP", "NC", "HFNC", "BIPAP", "CPAP", "TRACH_MASK", "VENTED"
    },

    "iv_access": {
        "NONE", "PIV", "MIDLINE", "PICC", "CVAD", "ARTLINE", "PA_LINE"
    },

    "nutrition": {
        "REGULAR", "CARDIAC", "RENAL", "DM_NO_CBGM", "DM_CBGM", "FR1L", 
        "FR1_5L", "FR2L", "SETUP", "NPO", "FEED_ASSIST", "ASP_PRECAUTIONS",
        "NGT_FEEDS", "OGT_FEEDS", "PEG_FEEDS", "TPN"
    },

    "drains_drsgs_integ":{
        "NONE", "SIMPLE_DRESSING", "ACRYLLIC_STERNUM", "PRIMAPORE_STERNUM", "PRIMAPORE_PERI",
        "TRACH_CARE", "CHEST_TUBE_CARE", "VAC_DRESSING", "COMPLEX_DRESSING", "PPM_DRESSING", "T&O",
        "SKIN_TEARS"
    },

    "elimination": {
        "NONE", "TOILET", "COMMODE", "URINAL", "FOLEY", "DIAPER", "INCONTINENT", "DIARRHEA",
        "HIGH_OUTPUT_STOOL", "SKIN_BREAKDOWN_RISK", "BOWEL_CARE", "COLOSTOMY"
    },

    "mobility": {
        "INDEP", "SUPERVISION",
        "AMB", "CANE", "WALKER",
        "AX1", "AX2",
        "WC", "BEDBOUND",
        "LIFT", "BRODA", "TOTAL_CARE"
        },
    
    "labs": {
        "ROUTINE", "K_ABNORMAL", "NA_ABNORMAL", "MG_ABNORMAL", "CA_ABNORMAL", "HGB_LOW", "PLT_LOW", "CREATININE_ABNORMAL", "WBC_ABNORMAL", "INR_ABNORMAL",
        "REPEAT_LABS", "FREQUENT_LABS", "ABG_MONITORING", "LACTATE_ELEVATED", "CRITICAL_LABS", "CONTINUOUS_CORRECTION"
    },

    "pro_involved":{
        "PT", "OT", "SW", "CARDIO", "NEPHRO", "DERM", "THROMBO", "NEURO", "URO", "ID", "GERI", 
        "DIET", "PULM", "RHEUM", "HEME", "DCPN", 
    },

    "safety": {
        "NONE", "FALL_RISK", "HIGH_FALL_RISK", "IMPULSIVE", "WANDERING", "PULLING_LINES", "CONFUSED_UNSAFE",
        "RESTRAINTS", "SITTER", "VIOLENT"
    },

    "medications": {
        "PO_ONLY", "IV_SIMPLE","IV_MULTIPLE","INSULIN_INFUSION",
        "TITRATABLE_DRIP", "MULTIPLE_TITRATABLE_DRIPS", "VASOPRESSOR","SEDATION_DRIP",
        "ANTIARRHYTHMIC_DRIP"
    },
    "turnover_update": {
        "STABLE", "POSSIBLE_TRANSFER", "TRANSFER_TODAY", "DISCHARGE_TODAY", "NEW_ADMISSION", "MULTIPLE_TURNOVER"
    }
}

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