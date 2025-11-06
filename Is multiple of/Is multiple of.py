print("Welcome! Choose two numbers and I will tell you if one is a multiple of the other")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 % num2 == 0:
    print(f"{num1} is a multiple of {num2}.")
elif num2 % num1 == 0:
    print(f"{num2} is a multiple of {num1}.")
else:
    print(f"{num1} is not a multiple of {num2}.")
