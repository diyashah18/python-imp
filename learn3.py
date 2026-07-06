name = input("Enter your name: ") 
weight = float(input("Enter your weight in kg: ")) 
height = float(input("Enter your height in meters: ")) 

bmi = weight / (height ** 2) 
print(f"{name}, your BMI is {bmi:.2f}") 

if bmi < 18.5: 
    print("You are underweight.") 
elif 18.5 <= bmi < 25: 
    print("You have a normal weight.") 
else: 
    print("You are overweight.")