# name = input("Enter your full name: ")
phone_number = input("Please Enter your Phone Number: ")

# result = len(name)
# result = name.find("a")
# result = name.rfind("a") # If the letter doesn't exist, it will return a -1. 
# name = name.capitalize() # Capitalize the First Letter
# name = name.upper() # Make all letters uppercase
# name = name.lower() # Make all letters lowercase
# result = name.isdigit() # Checks to see if the string ONLY contains digits, it will return True or False.
# result = name.isalpha() # Check to see if the string ONLY contains alphabets, it will return True or False. Numbers and White Spaces = False. 
# result = phone_number.count("-")
phone_number = phone_number.replace("-", " ")
print(phone_number)