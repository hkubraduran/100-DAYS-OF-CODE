# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmı = round(weight / (height * height))
if bmı < 18.5 :
    print(f"Your BMI is {bmı}, you are underweight.")
elif bmı > 18.5 and bmı < 25 :
    print(f"Your BMI is {bmı}, you have a normal weight.")
elif bmı > 25 and bmı < 30 :
    print(f"Your BMI is {bmı}, you are slightly overweight.")
elif bmı > 30 and bmı < 35 :
    print(f"Your BMI is {bmı}, you are obese.")
else:
    print(f"Your BMI is {bmı}, you are clinically obese.")