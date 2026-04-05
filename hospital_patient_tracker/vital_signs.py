
class VitalSigns:

    """A simple class recording the vital_signs of a patient"""

    def __init__(self, systolic_bp, diastolic_bp, heart_rate, oxygen_saturation, respiratory_rate, temperature):
        
        """Initialize all the components of the vital signs"""
        self.systolic_bp = systolic_bp
        self.diastolic_bp = diastolic_bp
        self.heart_rate = heart_rate
        self.oxygen_saturation = oxygen_saturation
        self.respiratory_rate = respiratory_rate
        self.temperature = temperature

    def display_vitals(self):
        print("\n---Displaying Vital Signs---")
        print(f"Blood Pressure: {self.systolic_bp}/{self.diastolic_bp} mm Hg")
        print(f"Heart Rate: {self.heart_rate} bpm")
        print(f"Respiratory Rate: {self.respiratory_rate} breaths/min")
        print(f"Oxygen Saturation: {self.oxygen_saturation}%")
        print(f"Temperature: {self.temperature}°C")

    def interpret_bp (self):
        """Interpreting the blood pressure and print it's classification"""
        if (self.systolic_BP <=120 and self.diastolic_BP<=80):
            print ("Blood pressure: Healthy")
        elif (120 <= self.systolic_BP <= 129) and self.diastolic_BP <80:
            print ("Blood pressure: Elevated")
        elif (130 <= self.systolic_BP <= 139) and (80 <= self.diastolic_BP <=89):
            print ("Blood pressure: Stage 1 Hypertension")
        elif (140 <= self.systolic_BP < 179) and ( self.diastolic_BP >= 90):
            print ("Blood pressure: Stage 2 Hypertension")
        elif (self.systolic_BP >= 180) and (self.diastolic_BP >=120):
            print ("Blood pressure: Hypertension Crisis")

    def interpret_hr(self):
        """Interpreting Heart Rate and print it's classification"""
        if self.heart_rate <60:
            print("Rhythm: Bradycardia")
        elif (60 <= self.heart_rate <100):
            print("Rhythm: Normal Heart Rate") 
        elif (self.heart_rate >= 100):
            print("Rhythm: Tachycardia")

    def interpret_spo2(self):
        """Interpreting Oxygen Saturation and printing it's classification"""
        if self.oxygen_saturation >= 92:
            print("Normal Oxygen Saturation")
        elif (88 <= self.oxygen_saturation  <=92): 
            print("Patient's Oxygen Saturation Unstable")
        else:
            print("Patient currently hypoxemic")

    def interpret_rr(self):
        """Interpreting Respiratory Rate and printing it's classification"""
        if self.respiratory_rate <12:
            print("Patient is bradypneic")
        elif (12 <= self.respiratory_rate <20):
            print("Patient is eupneic. Normal Breathing") 
        elif (self.respiratory_rate>= 20):
            print("Patient is tachypneic")

    def interpret_temperature(self):
        """Interpreting Temperature and printing it's classification"""
        if self.temperature <36.0:
            print("Patient is hypothermic")
        elif (36.0 <= self.temperature <38.0):
            print("Patient's temperature is normal") 
        elif (self.temperature >= 38.0):
            print("Patient is hyperthermic. The patient is having a fever!")

vitals1 = VitalSigns(110,90, 65, 18, 95, 36.5 )
