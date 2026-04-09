

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
        isolation = "N/A",
        level_intervention ="N/A",
        past_hx =None,
        allergies = None,
        type_sx ="N/A",
        procedures =None,
        neuro = "N/A",
        rhythm= "N/A",
        ventilation="N/A",
        iv_access="N/A",
        nutrition=None,
        dressings=None,
        elimination="N/A",
        mobility="N/A",
        labs=None,
        medications=None,
        issues=None,
        plans="N/A",
        pros_involved=None,
        home_screen="N/A",
        possible_dc="N/A",
        vital_signs = None
    ):
        self.unit = unit # CVU or CVICU
        self.room = room    #K0210
        self.name = name    #Joshua Visario
        self.mrn = mrn      #05091999
        self.age = age      #26
        self.gender = gender    #M
        self.admission_date = admission_date    #2026-04-05
        self.team_doctor = team_doctor  #Team 1 Cardiology
        self.diagnosis = diagnosis  #MVD

        self.isolation = isolation      #MRC
        self.level_intervention = level_intervention    #A
        self.past_hx = past_hx if past_hx else []  #['DM2', 'HTN' 'DLP']
        self.allergies = allergies if allergies else [] #['PNC','Vancomycin']
        self.type_sx = type_sx #CABGx4
        self.procedures = procedures if procedures else []# ['CXR:___, 'Cardiac Echo:___']
        self.neuro = neuro #AOx3
        self.rhythm = rhythm #'SR'
        self.ventilation = ventilation #RA
        self.iv_access = iv_access #L PIV
        self.nutrition = nutrition if nutrition else [] #['Cardiac', 'Diabetic']
        self.dressings = dressings if dressings else [] #['Sternum']
        self.elimination = elimination 
        self.mobility = mobility #Indep
        self.labs = labs if labs else [] #['K:__, Na+:__]
        self.medications = medications if medications else [] #['Lasix','ASA','Metoprolol']
        self.issues = issues if issues else [] #None
        self.plans = plans  #DC Soon
        self.pros_involved = pros_involved if pros_involved else []  #['SW','PT','OT]
        self.home_screen = home_screen #Lives alone
        self.possible_dc = possible_dc #2026-04-10
        self.vital_signs = vital_signs 

    def display_info(self):
        print(f"\n--- Patient {self.mrn} ---")
        print(f"Room: {self.room}")
        print(f"Name: {self.name}")
        print (f"MRN: {self.mrn}")
        print(f"Age/Gender: {self.age} / {self.gender}")
        print(f"Admission Date: {self.admission_date}")
        print(f"Doctor: {self.team_doctor}")
        print(f"Diagnosis: {self.diagnosis}")

        print(f"Isolation: {self.isolation}")
        print(f"Level of intervention: {self.level_intervention}")
        print(f"Past Hx: {self.past_hx}")
        print(f"Allergies: {self.allergies}")
        print(f"Surgery Type: {self.type_sx}")
        print(f"Procedures: {self.procedures}")
        print(f"Neuro: {self.neuro}")
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

#-------------------------
#Methods that updates the required attributes 
    #def update_room(self):


patient1 = Patient( 'K0210', 'Joshua Visario', 5091999, 26, 'M', '2026-04-05', 'Team 1 Cardiology','MVD', 'MRC', 'A', ['DM2', 'HTN', 'DLP'],
        ['PNC','Vancomycin'], 'CABGx4', ['CXR:___', 'Cardiac Echo:___'], 'AOX3', 'SR', 'RA', 'L PIV',['Cardiac', 'Diabetic'],['Sternum'], None,  
        'Indep', ['K:__', 'Na+:__'], ['Lasix','ASA','Metoprolol'],None, 'DC Soon', ['SW','PT','OT'], 'Lives alone', '2026-04-10')

patient1.display_info()