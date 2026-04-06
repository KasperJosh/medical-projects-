

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
        diagnosis,
        past_hx,
        allergies,
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
        possible_dc
    ):
        self.room = room    #K0210
        self.name = name    #Joshua Visario
        self.mrn = mrn      #05091999
        self.age = age      #26
        self.gender = gender    #M
        self.admission_date = admission_date    #2026-04-05
        self.isolation = isolation      #MRC
        self.level_intervention = level_intervention    #A
        self.team_doctor = team_doctor  #Team 1 Cardiology
        self.diagnosis = diagnosis  #MVD
        self.past_hx = past_hx  #['DM2', 'HTN' 'DLP']
        self.allergies = allergies #['PNC','Vancomycin']
        self.type_sx = type_sx #CABGx4
        self.procedures = procedures # ['CXR:___, 'Cardiac Echo:___']
        self.rhythm = rhythm #'SR'
        self.ventilation = ventilation #RA
        self.iv_access = iv_access #L PIV
        self.nutrition = nutrition #['Cardiac', 'Diabetic']
        self.dressings = dressings #['Sternum']
        self.elimination = elimination 
        self.mobility = mobility #Indep
        self.labs = labs #['K:__, Na+:__]
        self.medications = medications #['Lasix','ASA','Metoprolol']
        self.issues = issues #None
        self.plans = plans  #DC Soon
        self.pros_involved = pros_involved  #['SW','PT','OT]
        self.home_screen = home_screen #Lives alone
        self.possible_dc = possible_dc #2026-04-10


    def display_info(self):
        print(f"\n--- Patient {self.mrn} ---")
        print(f"Room: {self.room}")
        print(f"Name: {self.name}")
        print(f"Age/Gender: {self.age} / {self.gender}")
        print(f"Admission Date: {self.admission_date}")
        print(f"Doctor: {self.team_doctor}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Past Hx: {self.past_hx}")
        print(f"Allergies: {self.allergies}")
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
        print(f"Possible Discharge: {self.possible_dc}")
        print(f"Isolation: {self.isolation}")
        print(f"Level of Intervention: {self.level_intervention}")



patient1 = Patient( 'K0210', 'Joshua Visario', 5091999, 26, 'M', '2026-04-05', 'MRC', 'A', 'Team 1 Cardiology', 'MVD', ['DM2', 'HTN' 'DLP'],
        ['PNC','Vancomycin'], 'CABGx4', ['CXR:___', 'Cardiac Echo:___'], 'SR', 'RA', 'L PIV',['Cardiac', 'Diabetic'],['Sternum'], None,  
        'Indep', ['K:__', 'Na+:__'], ['Lasix','ASA','Metoprolol'],None, 'DC Soon', ['SW','PT','OT'], 'Lives alone', '2026-04-10')

patient1.display_info()