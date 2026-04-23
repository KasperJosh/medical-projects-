class Nurse:

    def __init__(
        self,
        name,
        nurse_id,
        experience_level,
        certifications,
        max_acuity_capacity,
        max_patients,
        is_new_grad,
        years_as_rn,
        years_in_cardiology,
        can_take_admission=True,
        empty_rooms_assigned=0,
        learning_needs=None,
        refused_patients=None,
        is_light_duty=False,
        pod= None
    ):

        self.name = name
        self.nurse_id = nurse_id

        # Inserting the pod the nurse is working in
        self.pod = pod 

        # Beginner / Intermediate / Expert
        self.experience_level = experience_level

        # Example: ["ACLS", "CRRT", "IABP", "BLS", "CCRN"]
        self.certifications = certifications

        # Max acuity nurse can safely handle
        self.max_acuity_capacity = max_acuity_capacity

        # Max patient amount a nurse can handle
        self.max_patients = max_patients

        # True if nurse is a new grad / newer RN
        self.is_new_grad = is_new_grad

        # Total years of RN experience
        self.years_as_rn = years_as_rn

        # Total years of cardiology / CVU experience
        self.years_in_cardiology = years_in_cardiology

        # Whether nurse can safely take an admission
        self.can_take_admission = can_take_admission

        # Empty rooms already assigned to nurse and awaiting admission
        self.empty_rooms_assigned = empty_rooms_assigned

        # Areas where nurse needs more exposure / learning
        # Example: ["POST_CATH", "CARDIAC_DRIPS", "CHEST_TUBES"]
        self.learning_needs = learning_needs if learning_needs is not None else []

        # Patient MRNs this nurse should not be assigned
        self.refused_patients = refused_patients if refused_patients is not None else []

        # True if nurse is on light duty
        self.is_light_duty = is_light_duty

        # Assigned patients
        self.assigned_patients = []

        # Running turnover workload score
        self.current_turnover = 0

        # Running acuity score
        self.current_acuity = 0

        # Running weighted workload score
        self.current_weighted = 0


    def adjusted_acuity_capacity(self):
        """
        Reduce safe acuity capacity if nurse already has empty rooms
        that may turn into admissions.

        Also reduce safe acuity if nurse is on light duty.
        """
        adjusted_capacity = self.max_acuity_capacity - (2 * self.empty_rooms_assigned)

        if self.is_light_duty:
            adjusted_capacity -= 3

        return max(0, adjusted_capacity)

    def adjusted_patient_capacity(self):
        """
        Reduce safe patient count if nurse is on light duty.
        """
        if self.is_light_duty:
            return max(1, self.max_patients - 1)

        return self.max_patients

    def can_take_patient(self, patient):
        """
        Check if nurse can safely take a patient based on:
        - max patient count
        - max acuity capacity
        - refused patient list
        """
        if patient.mrn in self.refused_patients:
            return False

        return (
            len(self.assigned_patients) < self.adjusted_patient_capacity() and
            (self.current_acuity + patient.acuity_score) <= self.adjusted_acuity_capacity()
        )

    def has_certification(self, cert):
        """
        Check if nurse has a required certification.
        """
        return cert in self.certifications

    def refuses_patient(self, patient):
        """
        Check if nurse refuses this patient.
        """
        return patient.mrn in self.refused_patients

    def assign_patient(self, patient):
        """
        Assign patient to nurse if safe to do so.
        """
        if not self.can_take_patient(patient):
            return False

        self.assigned_patients.append(patient)
        self.current_acuity += patient.acuity_score
        self.current_weighted += patient.total_weighted_score

        # Add turnover burden if patient has turnover_score
        if hasattr(patient, "turnover_score"):
            self.current_turnover += patient.turnover_score

        return True

    def display_assignment(self):
        print(f"\nNurse: {self.name}")
        print(f"Nurse ID: {self.nurse_id}")
        print(f"Experience Level: {self.experience_level}")
        print(f"Pod: {self.pod}")
        #print(f"New Grad: {self.is_new_grad}")
        #print(f"Light Duty: {self.is_light_duty}")
        #print(f"Years as RN: {self.years_as_rn}")
        #print(f"Years in Cardiology: {self.years_in_cardiology}")
        #print(f"Can Take Admission: {self.can_take_admission}")
        #print(f"Empty Rooms Assigned: {self.empty_rooms_assigned}")
        #print(f"Learning Needs: {self.learning_needs}")
        #print(f"Refused Patients: {self.refused_patients}")
        print(f"Total Acuity: {self.current_acuity}/{self.adjusted_acuity_capacity()}")
        print(f"Total Weighted: {self.current_weighted}")
        print(f"Total Turnover: {self.current_turnover}")
        print(f"Patient Count: {len(self.assigned_patients)}/{self.adjusted_patient_capacity()}")
        print("Patients:")

        if not self.assigned_patients:
            print(" - No patients assigned")

        for patient in self.assigned_patients:
            turnover_display = getattr(patient, "turnover_score", 0)
            print(
                f" - Room {patient.room}: {patient.name} "
                f"(Acuity: {patient.acuity_score}, Weighted: {patient.total_weighted_score}, Turnover: {turnover_display})"
            )