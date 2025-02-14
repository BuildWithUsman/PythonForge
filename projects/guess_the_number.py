import math
import random
import sys

number = random.randint(1, 25) # Generate a random number from 1 to 50
print(number) # Print that number

print("We are going to play a game called Guess The Number, you will only get 2 attempts!")
print("If you wish to cancel out of the game, please type E")
guess = int(input("Please a number betweeen 1 to 25: "))

print(type(guess))

if guess > 25 or guess < 1:
    print("You are entered a number outside of the range, exiting program")
    sys.exit
elif guess == number:
    print("Great job, you are correct!")
elif guess > number:
    print("You are too high!")
    new_guess = int(input("Please try again: "))
    if new_guess == number:
        print("You are correct!")
    else:
        print("Sorry you weren't able to guess the correct number!")
        sys.exit()
elif guess < number:
    print("You are too low!")
    new_guess = int(input("Please try again: "))
    if new_guess == number:
        print("You are correct!")
    else:
        print("Sorry you weren't able to guess the correct number!")
        sys.exit()
else:
    pass