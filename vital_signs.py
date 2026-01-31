#Code that records the vital signs of pts

print("Welcome to the Vital Signs Recorder!")
print("Please enter all the required information on the patients")



patient_name = str(input("Please enter the patient's name: "))
patient_MRN = int(input("Please enter the patient's MRN: "))
patient_BP = str(input("Please enter the patient's blood pressure: "))
patient_HR = int(input("PLease enter the patient's pulse rate: "))
patient_spO2 = int(input("Please enter the patient's oxygen saturation: "))
patient_rr = int(input("Please enter the patient's respiratory rate: "))
patient_temp = float(input("Please enter the patient's temperature: "))

BP_values = patient_BP.split("/")
systolic_BP = int(BP_values[0])
diastolic_BP = int(BP_values[1])

#Classifying Blood Pressures 
if (systolic_BP <=120 and diastolic_BP<=80):
    print ("Blood pressure: Healthy")
elif (120 <= systolic_BP <= 129) and diastolic_BP <80:
    print ("Blood pressure: Elevated")
elif (130 <= systolic_BP <= 139) and (80 <= diastolic_BP <=89):
    print ("Blood pressure: Stage 1 Hypertension")
elif (140 <=systolic_BP < 179) and (diastolic_BP >= 90):
    print ("Blood pressure: Stage 2 Hypertension")
elif (systolic_BP >= 180) and (diastolic_BP >=120):
    print ("Blood pressure: Hypertension Crisis")


#Classifying Cardiac Rhythms
#patient_HR = 59
if patient_HR <60:
    print("Rhythm: Bradycardia")
elif (60 <= patient_HR <100):
    print("Rhythm: Normal Heart Rate") 
elif (patient_HR >= 100):
    print("Rhythm: Tachycardia")


#Classifying Oxygen Saturation
patient_spO2 = 78
if patient_spO2 >= 92:
    print("Normal Oxygen Saturation")
elif (88 <= patient_spO2 <=92): 
    print("Patient's Oxygen Saturation Unstable")
else:
    print("Patient currently hypoxemic")