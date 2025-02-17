# name = input("Enter your full name: ")
# phone_number = input("Please Enter your Phone Number: ")

# result = len(name)
# result = name.find("a") # Find where the letter is located, starts from 0. Find Method looks for any character.
# result = name.rfind("a") # Reverse find where the letter is located, start from 0. If the letter doesn't exist, it will return a -1. 
# name = name.capitalize() # Capitalize the First Letter
# name = name.upper() # Make all letters uppercase
# name = name.lower() # Make all letters lowercase
# result = name.isdigit() # Checks to see if the string ONLY contains digits, it will return True or False.
# result = name.isalpha() # Check to see if the string ONLY contains alphabets, it will return True or False. Numbers and White Spaces = False. 
# result = phone_number.count("-") # Count how many times the character "-" shows up.
# phone_number = phone_number.replace("-", " ") # Find and Replace "-" with a white space " ".
# print(phone_number)

# Validate User Input Exercise 
# 1. username is no more than 12 characters. Use the len() method with a if statement. 
# 2. username must not contain spaces. Use the find() method with a if statement, remember if a character doesn't exist it will print -1. 
# 3. username must not contain digits. 

username = input("Enter a username: ")

username.isalpha() 

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain digits")
else:
    print(f"Welcome {username}")

