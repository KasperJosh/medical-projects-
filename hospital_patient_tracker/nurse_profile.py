
class Nurse:

    def __init__(self, name, nurse_id, experience_level, certifications, max_acuity_capacity):
        
        self.name = name
        self.nurse_id = nurse_id
        
        # Beginner / Intermediate / Expert
        self.experience_level = experience_level
        
        # Example: ["ACLS", "CRRT", "IABP", "BLS", "CCRN"]
        self.certifications = certifications
        
        # Max acuity nurse can safely handle
        self.max_acuity_capacity = max_acuity_capacity
        
        # Assigned patients
        self.assigned_patients = []
        
        # Running total acuity
        self.current_acuity = 0

    def assign_patient(self, patient):
        self.assigned_patients.append(patient)
        self.current_acuity += patient.acuity_score

    def can_take_patient(self, patient):
        return (self.current_acuity + patient.acuity_score) <= self.max_acuity_capacity

    def display_assignment(self):
        print(f"\nNurse: {self.name}")
        print(f"Total Acuity: {self.current_acuity}/{self.max_acuity_capacity}")
        print("Patients:")
        for p in self.assigned_patients:
            print(f" - {p.name} (Acuity: {p.acuity_score})")