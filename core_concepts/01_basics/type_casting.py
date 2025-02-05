# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), or bool().

name = "Bro Code"
age = 25
age2 = 35
gpa = 3.2 
is_student = True

# You can the type of a variable by utilizing type(variable_name)
# Example 

type(name) # If you run this as is, then it won't return anything back.
           # To print the type of variable on the screen, we need to use the print statement.

print(type(name), "\n")
print(type(age), "\n")
print(type(gpa), "\n")
print(type(is_student), "\n")

# Convert the GPA to a Integer 
gpa = int(gpa)
print(gpa)

# Convert the Age to a Float
age = float(age)
print(age)

# Convert the Age into a String 
age2 = str(age2) # Even though the output will be the same, the variable itself has actually changed into a Integer.
print(age2) # The reason why the output will remain the same is because 35 typed as a string is 35. You can think of it as this, "35". 
print(type(age2)) # To prove that it converted the variable into a string, we will use the type method to print it's variable type. 