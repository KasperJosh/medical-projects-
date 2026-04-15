
class Nurse:

    def __init__(self, name, nurse_id, experience_level, certifications, max_acuity_capacity, max_patients):
        
        self.name = name
        self.nurse_id = nurse_id
        
        # Beginner / Intermediate / Expert
        self.experience_level = experience_level
        
        # Example: ["ACLS", "CRRT", "IABP", "BLS", "CCRN"]
        self.certifications = certifications
        
        # Max acuity nurse can safely handle
        self.max_acuity_capacity = max_acuity_capacity

        # Max patient amount a nurse can handle
        self.max_patients = max_patients
        
        # Assigned patients
        self.assigned_patients = []
        
        # Running total acuity
        self.current_acuity = 0

    def can_take_patient(self, patient):
        return (
            len(self.assigned_patients) < self.max_patients and
            (self.current_acuity + patient.acuity_score) <= self.max_acuity_capacity
        )

    def has_certification(self, cert):
        return cert in self.certifications

    def assign_patient(self, patient):
        if not self.can_take_patient(patient):
            return False

        self.assigned_patients.append(patient)
        self.current_acuity += patient.acuity_score
        return True

    def display_assignment(self):
        print(f"\nNurse: {self.name}")
        print(f"Experience: {self.experience_level}")
        print(f"Total Acuity: {self.current_acuity}/{self.max_acuity_capacity}")
        print(f"Patient Count: {len(self.assigned_patients)}/{self.max_patients}")
        print("Patients:")
        for p in self.assigned_patients:
            print(f" - Room {p.room}: {p.name} (Acuity: {p.acuity_score})")

    