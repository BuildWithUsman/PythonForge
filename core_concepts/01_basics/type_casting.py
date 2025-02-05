# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), or bool().

# Defining variables 
name = "Bro Code"
name2 = ""
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

# Convert the Age2 into a String 
age2 = str(age2) # Even though the output will be the same, the variable itself has actually changed into a Integer.
print(age2) # The reason why the output will remain the same is because 35 typed as a string is 35. You can think of it as this, "35". 
print(type(age2)) # To prove that it converted the variable into a string, we will use the type method to print it's variable type. 

# It is important to know that when typecasting Integers to Strings, you can no longer do arithmetric expressions with them. 
# Example - THIS WILL NOT RUN!! It will error out with the following error message:
# TypeError: can only concatenate str (not "int") to str
# age2 += 1 # This is the same thing as age2 = age2 + 1
# print(age2)

# However though, you add quotes around the 1 then it will work but it will display it as 351 because age2 is a string. 
# Example 
age2 += "1"
print(age2)

# Convert String into a Boolean 
# When converting a variable type into a boolean type, the output will always be True unless the variable is empty. 
# Doesn't matter what variable contains.
# We can this to check if a user gave their name or any other value. 
# Examples

name = bool(name)
print(name)

name2 = bool(name2)
print(name2)

# If the user gave their name, meaning name2 variable isn't emtpy then it will print out "User gave their name!"
# If the user didn't give their name, it will print out "User didn't give their name"
if name2:
    print(f"User gave their name!") 
else:
    print("User didn't give their name")