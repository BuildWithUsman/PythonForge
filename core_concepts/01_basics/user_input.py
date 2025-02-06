# input() = A function that prompts the user to enter data. 
#           Returns the entered data as a string. 

#input() #Running this by itself will prompt the user to enter something but don't display any text to tell the user what to enter.

name = input("What is your name?: ")
age = input("How old are you?: ")

# age = age + 1 If you run this code, it will error because of the following error message:
#               TypeError: can only concatenate str (not "int") to str
#               To fix this error, we need to type cast the string into a integer since we can only do arithmetric expressions with ints or floats.

age = int(age)
age = age + 1

# If you wnat to simply the type casting or concatenating, you can do the following: 
# Example:

new_age = int(input("How old will you be in 5 years?: ")) # Doing this already concatenates the variable from a string to integer or floats.

print(f"Hello {name}")
print("Happy Birthday")
print(f"You are {age} years old")
print(f"5 years from now, you will be: {new_age}")

### Exercises ###

# Exercise 1 - Rectangle Area Calc

length = float(input("Enter the legnth: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is: {area}㎠")


