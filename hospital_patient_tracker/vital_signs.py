
class VitalSigns:

    """A simple Vital Signs class and interpreting the meaning of it"""

    def __init__(self, systolic_bp, diastolic_bp, heart_rate, respiratory_rate, oxygen_saturation, temperature):
        
        """Initialize all the components of the vital signs"""
        self.systolic_bp = systolic_bp
        self.diastolic_bp = diastolic_bp
        self.heart_rate = heart_rate
        self.respiratory_rate = respiratory_rate
        self.oxygen_saturation = oxygen_saturation
        self.temperature = temperature

    def display_vitals(self):
        print("\n---Displaying Vital Signs---")
        print(f"Blood Pressure: {self.systolic_bp}/{self.diastolic_bp} mmHg")
        print(f"Heart Rate: {self.heart_rate} bpm")
        print(f"Oxygen Saturation: {self.oxygen_saturation} %")
        print(f"Respiratory Rate: {self.respiratory_rate} breaths/min")
        print(f"Temperature: {self.temperature} °C")

    def interpret_bp (self):
        """Interpreting the blood pressure and print it's classification"""
        if (self.systolic_bp <=120 and self.diastolic_bp<=80):
            return ("Blood pressure: Healthy")
        elif (120 <= self.systolic_bp <= 129) and self.diastolic_bp <80:
            return ("Blood pressure: Elevated")
        elif (130 <= self.systolic_bp <= 139) or (80 <= self.diastolic_bp <=89):
            return ("Blood pressure: Stage 1 Hypertension")
        elif (140 <= self.systolic_bp < 179) or (self.diastolic_bp >= 90):
            return ("Blood pressure: Stage 2 Hypertension")
        elif (self.systolic_bp >= 180) or (self.diastolic_bp >=120):
            return ("Blood pressure: Hypertension Crisis")

    def interpret_hr(self):
        """Interpreting Heart Rate and print it's classification"""
        if self.heart_rate <60:
            return ("Rhythm: Bradycardia")
        elif (60 <= self.heart_rate <100):
            return ("Rhythm: Normal Heart Rate") 
        elif (self.heart_rate >= 100):
            return ("Rhythm: Tachycardia")

    def interpret_spo2(self):
        """Interpreting Oxygen Saturation and printing it's classification"""
        if self.oxygen_saturation >= 92:
            return ("Normal Oxygen Saturation")
        elif (88 <= self.oxygen_saturation  <=92): 
            return ("Patient's Oxygen Saturation Unstable")
        else:
            return ("Patient currently hypoxemic")

    def interpret_rr(self):
        """Interpreting Respiratory Rate and printing it's classification"""
        if self.respiratory_rate <12:
            return ("Patient is bradypneic")
        elif (12 <= self.respiratory_rate <20):
            return ("Patient is eupneic. Normal Breathing") 
        elif (self.respiratory_rate>= 20):
            return ("Patient is tachypneic")

    def interpret_temperature(self):
        """Interpreting Temperature and printing it's classification"""
        if self.temperature <36.0:
            return ("Patient is hypothermic")
        elif (36.0 <= self.temperature <38.0):
            return ("Patient's temperature is normal") 
        elif (self.temperature >= 38.0):
            return ("Patient is hyperthermic. The patient is having a fever!")

vitals1 = VitalSigns(110,90, 65, 18, 95, 36.5 )
vitals1.display_vitals()
vitals1.interpret_bp()