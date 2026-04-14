



class Patient:
    """Representing a patient on the unit"""


    def __init__(
        self,
        unit,
        room,
        name,
        mrn,
        age,
        gender,
        admission_date,
        team_doctor,
        diagnosis,


        isolation_status="NONE",
        level_of_intervention="A",
        pmhx=None,
        allergies=None,
        type_sx="N/A",
        procedures_tests=None,


        hemodynamic_status="STABLE",
        cardiac_status="NONE",
        respiratory_status="RA",
        neurological_status="AOX3",
        lab_instability="ROUTINE",
        safety_risk="NONE",
        behaviour_cooperation="COOPERATIVE",
        medication_complexity="PO_ONLY",
        cbgm_frequency="NONE",
        monitoring_frequency="ROUTINE",


        iv_access="NONE",
        nutrition="REGULAR",
        wounds_dressings="NONE",
        elimination="NONE",
        mobility="INDEP",
        pain_management="CONTROLLED",
        communication="NONE",
        family_social="INDEP",
        blood_test_frequency="DAILY",


        medications=None,
        issues=None,
        plans="N/A",
        pro_involved=None,
        home_screen="N/A",
        turnover="STABLE",
        vital_signs=None,
        special_flags=None
    ):
        self.unit = unit
        self.room = room
        self.name = name
        self.mrn = mrn
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.team_doctor = team_doctor
        self.diagnosis = diagnosis


        self.isolation_status = isolation_status
        self.level_of_intervention = level_of_intervention
        self.pmhx = pmhx if pmhx else []
        self.allergies = allergies if allergies else []
        self.type_sx = type_sx
        self.procedures_tests = procedures_tests if procedures_tests else []


        self.hemodynamic_status = hemodynamic_status
        self.cardiac_status = cardiac_status
        self.respiratory_status = respiratory_status
        self.neurological_status = neurological_status
        self.lab_instability = lab_instability
        self.safety_risk = safety_risk
        self.behaviour_cooperation = behaviour_cooperation
        self.medication_complexity = medication_complexity
        self.cbgm_frequency = cbgm_frequency
        self.monitoring_frequency = monitoring_frequency


        self.iv_access = iv_access
        self.nutrition = nutrition
        self.wounds_dressings = wounds_dressings
        self.elimination = elimination
        self.mobility = mobility
        self.pain_management = pain_management
        self.communication = communication
        self.family_social = family_social
        self.blood_test_frequency = blood_test_frequency


        self.medications = medications if medications else []
        self.issues = issues if issues else []
        self.plans = plans
        self.pro_involved = pro_involved if pro_involved else []
        self.home_screen = home_screen
        self.turnover = turnover
        self.vital_signs = vital_signs
        self.special_flags = special_flags if special_flags else []


        self.acuity_score = 0
        self.acuity_level = "Not scored"
        self.acuity_breakdown = {}


    def display_info(self):
        print(f"\n--- Patient {self.mrn} ---")
        print(f"Unit: {self.unit}")
        print(f"Room: {self.room}")
        print(f"Name: {self.name}")
        print(f"MRN: {self.mrn}")
        print(f"Age/Gender: {self.age} / {self.gender}")
        print(f"Admission Date: {self.admission_date}")
        print(f"Doctor: {self.team_doctor}")
        print(f"Diagnosis: {self.diagnosis}")


        print(f"Isolation Status: {self.isolation_status}")
        print(f"Level of Intervention: {self.level_of_intervention}")
        print(f"Past Hx: {self.pmhx}")
        print(f"Allergies: {self.allergies}")
        print(f"Surgery Type: {self.type_sx}")
        print(f"Procedures/Tests: {self.procedures_tests}")


        print(f"Hemodynamic Status: {self.hemodynamic_status}")
        print(f"Cardiac Status: {self.cardiac_status}")
        print(f"Respiratory Status: {self.respiratory_status}")
        print(f"Neurological Status: {self.neurological_status}")
        print(f"Lab Instability: {self.lab_instability}")
        print(f"Safety Risk: {self.safety_risk}")
        print(f"Behaviour/Cooperation: {self.behaviour_cooperation}")
        print(f"Medication Complexity: {self.medication_complexity}")
        print(f"CBGM Frequency: {self.cbgm_frequency}")
        print(f"Monitoring Frequency: {self.monitoring_frequency}")


        print(f"IV Access: {self.iv_access}")
        print(f"Nutrition: {self.nutrition}")
        print(f"Wounds/Dressings: {self.wounds_dressings}")
        print(f"Elimination: {self.elimination}")
        print(f"Mobility: {self.mobility}")
        print(f"Pain Management: {self.pain_management}")
        print(f"Communication: {self.communication}")
        print(f"Family/Social: {self.family_social}")
        print(f"Blood Test Frequency: {self.blood_test_frequency}")


        print(f"Medications: {self.medications}")
        print(f"Issues: {self.issues}")
        print(f"Plans: {self.plans}")
        print(f"Professionals Involved: {self.pro_involved}")
        print(f"Home Situation: {self.home_screen}")
        print(f"Turnover: {self.turnover}")
        print(f"Special Flags: {self.special_flags}")


        print(f"Acuity Score: {self.acuity_score}")
        print(f"Acuity Level: {self.acuity_level}")
        print(f"Acuity Breakdown: {self.acuity_breakdown}")


#-------------------------
#Methods that updates the required attributes
    #def update_room(self):

#patient1 = Patient(
#    unit="CVU",
#    room="K0210",
#    name="Joshua Visario",
#    mrn=5091999,
#    age=26,
#    gender="M",
#    admission_date="2026-04-05",
#    team_doctor="Team 1 Cardiology",
#    diagnosis="CABG",

#    isolation_status="MRC",
#    level_of_intervention="A",
#    pmhx=["DM2", "HTN", "DLP"],
#    allergies=["PNC", "VANCOMYCIN"],
#    type_sx="CABGX4",
#    procedures_tests=["CXR", "TTE"],

#    hemodynamic_status="STABLE",
#    cardiac_status="NSR",
#    respiratory_status="RA",
#    neurological_status="AOX3",
#    lab_instability="ROUTINE",
#    safety_risk="FALL_RISK",
#    behaviour_cooperation="COOPERATIVE",
#    medication_complexity="IV_SIMPLE",
#    cbgm_frequency="ACHS",
#    monitoring_frequency="ROUTINE",

#    iv_access="PIV",
#    nutrition="DM_CBGM",
#    wounds_dressings="STERNAL_DRESSING",
#    elimination="NONE",
#    mobility="AX1",
#    pain_management="CONTROLLED",
#    communication="NONE",
#    family_social="INDEP",
#    blood_test_frequency="DAILY",

#    medications=["LASIX", "ASA", "METOPROLOL"],
#    issues=[],
#    plans="DC SOON",
#    pro_involved=["SW", "PT", "OT"],
#    home_screen="LIVES ALONE",
#    turnover="POSSIBLE_TRANSFER",
#    vital_signs=None,
#    special_flags=[]
#)

#patient1.display_info()

