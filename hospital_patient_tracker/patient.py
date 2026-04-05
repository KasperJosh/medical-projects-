

class Patient:
    """Representing a patient on the unit"""
    
    def __init__(
        self,
        room,
        name,
        mrn,
        age,
        gender,
        admission_date,
        isolation,
        level_intervention,
        team_doctor,
        diagnostic,
        past_hx,
        allergy,
        type_sx,
        procedures,
        rhythm,
        ventilation,
        iv_access,
        nutrition,
        dressings,
        elimination,
        mobility,
        labs,
        medications,
        issues,
        plans,
        pros_involved,
        home_screen,
        possible_DC
    ):
        self.room = room
        self.name = name
        self.mrn = mrn
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.isolation = isolation
        self.level_intervention = level_intervention
        self.team_doctor = team_doctor
        self.diagnostic = diagnostic
        self.past_hx = past_hx
        self.allergy = allergy
        self.type_sx = type_sx
        self.procedures = procedures
        self.rhythm = rhythm
        self.ventilation = ventilation
        self.iv_access = iv_access
        self.nutrition = nutrition
        self.dressings = dressings
        self.elimination = elimination
        self.mobility = mobility
        self.labs = labs
        self.medications = medications
        self.issues = issues
        self.plans = plans
        self.pros_involved = pros_involved
        self.home_screen = home_screen
        self.possible_DC = possible_DC


        def display_info(self):
            print(f"\n--- Patient {self.mrn} ---")
            print(f"Room: {self.room}")
            print(f"Name: {self.name}")
            print(f"Age/Gender: {self.age} / {self.gender}")
            print(f"Admission Date: {self.admission_date}")
            print(f"Doctor: {self.team_doctor}")
            print(f"Diagnosis: {self.diagnostic}")
            print(f"Past Hx: {self.past_hx}")
            print(f"Allergies: {self.allergy}")
            print(f"Surgery Type: {self.type_sx}")
            print(f"Procedures: {self.procedures}")
            print(f"Rhythm: {self.rhythm}")
            print(f"Ventilation: {self.ventilation}")
            print(f"IV Access: {self.iv_access}")
            print(f"Nutrition: {self.nutrition}")
            print(f"Dressings: {self.dressings}")
            print(f"Elimination: {self.elimination}")
            print(f"Mobility: {self.mobility}")
            print(f"Labs: {self.labs}")
            print(f"Medications: {self.medications}")
            print(f"Issues: {self.issues}")
            print(f"Plans: {self.plans}")
            print(f"Professionals Involved: {self.pros_involved}")
            print(f"Home Situation: {self.home_screen}")
            print(f"Possible Discharge: {self.possible_DC}")
            print(f"Isolation: {self.isolation}")
            print(f"Level of Intervention: {self.level_intervention}")



        #def admit_patient()