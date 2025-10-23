# BMI Calculator with Category
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI: {:.2f}".format(bmi))

# BMI Category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)
