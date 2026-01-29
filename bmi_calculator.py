# Generates the BMI of the input height and weight 

print("Welcome to the BMI calculator!")

height = float(input("Please enter your height in meters: "))
weight = float(input ("Please enter your weight in kilograms: "))


bmi = float(weight / (height**2))


print("Your BMI is: " + str(round(bmi,2)))


if (bmi < 18.5):
    print("Weight Status: Underweight")
elif (bmi >=18.5 and bmi <=24.9):
    print("Weight Status: Healthy Weight")
elif (bmi >=25.0 and bmi <=29.9):
    print("Weight Status: Overweight")
elif (bmi >=30.0 and bmi <=34.9):
    print("Weight Status: Obese Class 1")
elif (bmi >=35.0 and bmi <=39.9):
    print("Weight Status: Obese Class 2")
else:
    print("Weight Status: Obese Class 3")

