#report_standards.py is a file so that I have standardized values in the report


# report_standards.py

STANDARD_FIELDS = {
    "isolation": {
        "LRC", "MRC", "HRC", "CDIFF", "MDRO", "BEDBUGS", "MRSA", "NONE"
    },

    "level_of_intervention": {
        "A", "B", "C", "D"
    },

    "pmhx": {
        "DM2", "DLP", "HTN", "HLP", "CAD", "CHF", "COPD", "CKD", "AFIB", "CVA"
    },

    "labs": {
        "NA", "K", "HGB", "WBC", "PLT", "CR", "UREA", "INR", "PTT", "MG", "CA", "TROP"
    },

    "rhythm": {
        "NSR", "SB", "ST", "AFLUTTER", "AFIB", "JUNCTIONAL",
        "1AVB", "2AVB1", "2AVB2", "3AVB",
        "NSVT", "VT", "VFIB", "PAC", "PVC"
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
    }
}