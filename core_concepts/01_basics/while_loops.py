# while loop = execute some code WHILE some condition remains true. 

name = input("Enter your name: ")

# if name == "": 
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

# If we want the user to be continuously prompted for a input, we will use a While Loop 

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") # You need a exit statement or else, the while loop will never exit out. 

print(f"Hello {name}")