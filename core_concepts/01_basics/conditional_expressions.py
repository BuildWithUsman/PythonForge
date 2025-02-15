# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of the two values based on a condition 
#                          X if condition else Y

num = 5

print("Positive" if num > 0 else "Negative")


new_num = 7 

result = "EVEN" if new_num % 2 == 0 else "ODD"

print(result)

a = 6 
b = 7

max_num = a if a > b else b
min_num = a if a < b else b