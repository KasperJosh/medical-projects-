patients = {
    'patient1': {
        'first_name': 'joshua',
        'last_name': 'visario',
        'patient_id': 44800,
        'patient_age': 26,
        'patient_gender': 'male',
        'admitting_service': 'cardiology',
        'vital_signs': {
            'systolic_BP': 120,
            'diastolic_BP': 80,
            'heart_rate': 60,
            'respiratory_rate': 16,
            'spO2': 94
            }
        },

    'patient2': {
        'first_name': 'celine',
        'last_name': 'nguyen',
        'patient_id': 123456,
        'patient_age': 28,
        'patient_gender': 'female',
        'admitting_service': 'cardiology',
        'vital_signs': {
            'systolic_BP': 130,
            'diastolic_BP': 90,
            'heart_rate': 90,
            'respiratory_rate': 14,
            'spO2': 90
            }
        },

    'patient3': {
        'first_name': 'antoine',
        'last_name': 'toso',
        'patient_id': 142536,
        'patient_age': 33,
        'patient_gender': 'male',
        'admitting_service': 'cardiology',
        'vital_signs': {
            'systolic_BP': 150,
            'diastolic_BP': 60,
            'heart_rate': 110,
            'respiratory_rate': 22,
            'spO2': 88
            }
        } 
}

for patient, patient_info in patients.items():

    print(f"\nPatient Number: {patient.title()}")
    full_name = f"{patient_info['first_name']} {patient_info['last_name']}"
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tPatient ID: {patient_info['patient_id']}")
    print(f'\tPatient Age: {patient_info['patient_age']}')
    print(f'\tPatient Gender: {patient_info['patient_gender'].title()}')
    print(f'\tAdmitting Department: {patient_info['admitting_service'].title()}')
    print(f'\tCurrent Vital Signs: ')

    vitals = patient_info['vital_signs']
    print(f'\t\tBlood pressure: {vitals['systolic_BP']}/{vitals['diastolic_BP']}')
    print(f'\t\tHeart Rate: {vitals['heart_rate']} bpm')
    print(f'\t\tRespiratory Rate: {vitals['respiratory_rate']}')
    print(f'\t\tOxygen Saturation: {vitals['spO2']} %')