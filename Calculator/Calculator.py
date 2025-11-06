num1 = float(input("Enter the first number: "))

op = input("Enter an operation (+, -, *, /): ")

num2 = float(input("Enter the second number: "))

if op == "+":
    result = num1 + num2
    print("Result:", result)
elif op == "-":
    result = num1 - num2
    print("Result:", result)
elif op == "*":
    result = num1 * num2
    print("Result:", result)
elif op == "/":

    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operation. Please use +, -, *, or /.")
