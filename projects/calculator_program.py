# Python Calculator 

operator = input("Enter an operator (+, -, *, or /): ")
num1 = float(input("Enter the 1st Number: ")) ## If you don't type cast, the variables (num1 and num2) then it will concatenate them as stirngs.
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