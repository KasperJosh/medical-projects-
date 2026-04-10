
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
            return ("Heart Rate: Bradycardia")
        elif (60 <= self.heart_rate <100):
            return ("Heart Rate: Normal Heart Rate") 
        elif (self.heart_rate >= 100):
            return ("Heart Rate: Tachycardia")

    def interpret_spo2(self):
        """Interpreting Oxygen Saturation and printing it's classification"""
        if self.oxygen_saturation >= 92:
            return ("Oxygen Saturation Status: Normal")
        elif (88 <= self.oxygen_saturation  <=92): 
            return ("Oxygen Saturation Status: Dropping")
        else:
            return ("Oxygen Saturation Status: Low")

    def interpret_rr(self):
        """Interpreting Respiratory Rate and printing it's classification"""
        if self.respiratory_rate <12:
            return ("Respiration Rate Status: Bradypneic")
        elif (12 <= self.respiratory_rate <20):
            return ("Respiration Rate Status: Normal Breathing") 
        elif (self.respiratory_rate>= 20):
            return ("Respiration Rate Status: Tachypneic")

    def interpret_temperature(self):
        """Interpreting Temperature and printing it's classification"""
        if self.temperature <36.0:
            return ("Patient is hypothermic")
        elif (36.0 <= self.temperature <38.0):
            return ("Patient's temperature is normal") 
        elif (self.temperature >= 38.0):
            return ("Patient is hyperthermic. The patient is having a fever!")

    def calculate_mean_arterial_pressure(self):
        mean_arterial_pressure = (self.systolic_bp + (2*self.diastolic_bp))//3
        return (f"Patient's MAP: {mean_arterial_pressure}")

    
    def is_unstable(self):
        return (
            self.oxygen_saturation < 90 or
            self.systolic_bp < 90 or
            self.heart_rate < 50 or self.heart_rate > 130 or
            self.temperature >39
        )
    
    def overall_status(self):
        return "UNSTABLE " if self.is_unstable() else "STABLE"

    # Earning Warning Score (In Progress)
    def early_warning_score(self):
        score = 0

        # Heart Rate
        if self.heart_rate < 40 or self.heart_rate > 130:
            score +=3
        elif 110 <= self.heart_rate <=130:
            score +=2
        
        # BP
        if self.systolic_bp <90:
            score +=3
        
        # Temp
        if self.temperature > 38.5 or self.temperature <35:
            score +=2
        
        return score 




#vitals1 = VitalSigns(110,70, 65, 18, 95, 36.5 )
#vitals1.display_vitals()
#print(vitals1.interpret_bp())
#print(vitals1.overall_status())
#print(vitals1.calculate_mean_arterial_pressure())