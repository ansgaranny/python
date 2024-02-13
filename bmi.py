weight = float(input("Enter your weight in Kilograms "))
height = float(input("Enter your height in metres"))
bmi = weight/(height**2)

if bmi <= 18.2:
    category = "underweight"
elif 18.4 <= bmi <= 25.9:
    category = "normal"
elif 26.0 <= bmi <= 41.9:
    category = "overweight"

else:
    category = "obese"
print(f"your BMI is {bmi} and your category is {category}")
