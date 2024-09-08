print("Welcome to the BMI Calculator")

# Input weight and height from the user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category and print result
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("Your weight is normal")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are extremely obese")
