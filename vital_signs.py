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

