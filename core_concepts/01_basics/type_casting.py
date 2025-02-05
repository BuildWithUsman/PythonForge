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

#Convert the Age into a String 
age2 = str(age2)
print(age2)