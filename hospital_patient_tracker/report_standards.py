#report_standards.py is a file so that I have standardized values in the report


STANDARD_FIELDS = {
    "isolation": {
        "LRC", "MRC", "HRC", "CDIFF", "CDIFF-R/O", "MDRO", "BEDBUGS", "MRSA", "NONE", "TB-R/O"
    },

    "level_of_intervention": {
        "A", "B", "C", "D"
    },

    "diagnosis": {
        "NSTEMI", "STEMI", "ACS", "AS", "CHF", "CHFE" "SYNCOPE", "FAF", "BVHF", "PNA", "UTI", "E.CABG", "CABG", "ADHF", "PH"
    },

    "pmhx": {
        "DM2", "DLP", "HTN", "HLP", "CAD", "CHF", "COPD", "CKD", "AFIB", "CVA", "CANCER", "OP", "PH"
    },

    "neuro": { "AOX3", "AOX2", "AOX1", "CONFUSED", "DELIRIUM", "AGITATED"
    },
    "rhythm": {
        "NSR", "SB", "ST", "AFLUTTER", "AFIB", "JUNCTIONAL",
        "1AVB", "2AVB1", "2AVB2", "3AVB",
        "NSVT", "VT", "VFIB", "PAC", "PVC", "NONE"
    },

    "ventilation": {
        "RA", "NP", "BIPAP", "CPAP", "NC", "VENTED"
    },

    "iv_access": {
        "PIV", "CVAD", "PICC", "ARTLINE", "PA LINE", "NONE"
    },

    "nutrition": {
        "CARDIAC", "DM-No-CBGM", "DM-CBGM", "FR1L", "FR1.5L", "FR2L", "NPO", "REGULAR"
    },

    "elimination": {
        "FOLEY", "DIAPER", "URINAL", "TOILET", "COMMODE", "NONE"
    },

    "mobility": {
        "INDEP", "AX1", "AX2", "WALKER", "CANE", "LIFT", "AMB" , "WC", "SUP"
    },
    
    "labs": {
        "NA", "K", "HGB", "WBC", "PLT", "CR", "UREA", "INR", "PTT", "MG", "CA", "TROP"
    },

    "pro_involved":{
        "PT", "OT", "SW", "CARDIO", "NEPHRO", "DERM", "THROMBO", "NEURO", "URO", "ID", "GERI", 
        "DIET", "PULM", "RHEUM", "HEME", "DCPN", 
    }
}

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