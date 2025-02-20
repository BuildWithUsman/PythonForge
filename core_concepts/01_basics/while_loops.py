# while loop = execute some code WHILE some condition remains true. 

# name = input("Enter your name: ")

# if name == "": 
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

# Example #1 - Name 
# If we want the user to be continuously prompted for a input, we will use a While Loop 

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ") # You need a exit statement or else, the while loop will never exit out. 

# print(f"Hello {name}")

# Example #2 - Age

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# Example #3 - Food 

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("Bye!")

# # Example #4 - Type a number between 1 and 10

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid.")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")

# Example #3 - Food, Cleaner Way to Write the Code

food = input("Enter a food you like (q to quit): ")

while food.lower() != "q": # Converts the string into lowercase, in case the user enters uppercase Q. 
                           # And You Don't Need to Write "not food ==", != is the simplier way and the same thing.
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Bye!")