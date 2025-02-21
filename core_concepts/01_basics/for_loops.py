# for loops = Execute a block of code for a fixed number of times. 
#             You can iterate over a range, stirng, sequence, etc. 

# Example #1 - Printing numbers 1 to 10. 
# for x in range(1, 11): # Second number mentioned in the range is exlcusive, so if you want to print 1 to 10 your end number would 11.
#                        # X is the variable storing the value, you can also use counter instead of x as the variable. 
#     print(x)

# Example #2 - Printing numbers 1 to 10 Reversed.
# for x in reversed(range(1, 11)): # To print the numbers 1 to 10 reversed you would use "reversed" and enclose it within the range.   
#     print(x)

# print("Happy New Year!")

# Example 3 - Printing numbers 1 to 10 but using the step function to skip numbers.
# for x in range(1, 11, 3): # To print the numbers 1 to 10 reversed you would use "reversed" and enclose it within the range.   
#     print(x)

# Example 4 - Iterate over String 
# credit_card = "1234-5678-9012-3456"

# for x in credit_card: # X represents our current position, starting at 0 and progressing until the end of the string. 0 in our example is 1.
#     print(x)

# Example 5 - Skip over a Iteration, for example if I want to skip the number 13 when printing 1 to 20. 
for x in range(1, 21):
    if x == 13:
        continue # Continue is a keyword that is used inside of a for loop to skip a iteration of something. 
    else:
        print(x)