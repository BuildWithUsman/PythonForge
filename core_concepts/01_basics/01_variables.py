# Variable(s) = A container for a value (string, integer, float, and boolean)
# A Variable behaves as if it was the value it contains 

# In this case, the variables below are called Strings.
# Strings
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

# Integers - they are whole numbers and cannot be in quotes. If they are in quotes, then they would be classified as a string. Can be used in arithmetic expressions.
age = 25
quantity = 3
num_of_students = 30

# Float - is a number, but it contains a decimal portion.
price = 10.99
gpa = 3.2
distance = 5.5

# Boolean - is either true or false and first letters are capital. Most commonly used with if-statemnts and etc. See example below. 
is_student = False
for_sale = False
is_online = True

# You can use this method to print out onto the terminal. 
print(first_name) # You can use this method to print out onto the terminal. 

# Or you can use the "f-string", with the "f-string" method you can write a Python expression between { and } characters that can refer to variables or literal values. 
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

print(f"\n") # You can use "\n" to add a line break. 

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

print(f"\n")

print(f"The price is ${price}.")
print(f"Your GPA is: {gpa}.")
print(f"You ran {distance} miles.")

print(f"\n")

print(f"Are you a student?: {is_student}")

if is_student:
    print(f"You are a student.")
else:
    print(f"You are NOT a student.") 

if for_sale:
    print("That item is for sale.")
else:
    print("That item is NOT available.")

if is_online:
    print("You are online.")
else: 
    print("You are offline.")