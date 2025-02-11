# Python Calculator 

operator = input("Enter an operator (+, -, *, or /): ")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*": 
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else: 
    print("Please Enter a valid operator")