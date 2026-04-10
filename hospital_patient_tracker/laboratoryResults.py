
class LaboratoryResults:
    
    def __init__(self, hemoglobin, wbc, platelets, sodium, potassium, creatinine, glucose):
        self.hemoglobin = hemoglobin
        self.wbc = wbc
        self.platelets = platelets
        self.sodium = sodium
        self.potassium = potassium
        self.creatinine = creatinine
        self.glucose = glucose

    def interpret_potassium(self):
        if self.potassium < 3.5:
            return "Low potassium"
        elif self.potassium > 5.0:
            return "High potassium"
        return "Normal potassium"

    def interpret_sodium(self):
        if self.sodium < 135:
            return "Low sodium"
        elif self.sodium > 145:
            return "High sodium"
        return "Normal sodium"

    def abnormal_labs_summary(self):
        abnormalities = []

        if self.hemoglobin < 120:
            abnormalities.append("Low hemoglobin")
        if self.wbc > 11:
            abnormalities.append("High WBC")
        if self.platelets < 150:
            abnormalities.append("Low platelets")
        if self.creatinine > 110:
            abnormalities.append("High creatinine")

        abnormalities.append(self.interpret_potassium())
        abnormalities.append(self.interpret_sodium())

        return [lab for lab in abnormalities if "Normal" not in lab]