import math
import random

number = random.randint(1, 25) # Generate a random number from 1 to 50
print(number) # Print that number

print("We are going to play a game called Guess The Number")
guess = int(input("Please a number betweeen 1 to 25: "))

print(type(guess))

if guess == number:
    print("Great job, you are correct!")
elif guess > number:
    print("You are too high!")
    new_guess = int(input("Please a number betweeen 1 to 25: "))

elif guess < number:
    print("You are too low!")
    new_guess = int(input("Please a number betweeen 1 to 25: "))
else:
    pass