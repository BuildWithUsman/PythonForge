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

print(f"Hello {name}")
print("Happy Birthday")
print(f"You are {age} years old")




