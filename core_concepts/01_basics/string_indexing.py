# Indexing = Accessing elements of a sequence using [] (indexing operator)
#            [start : end : step] - 3 Fields we can fill in, start, end, and step. 
#            If you have only field listed, without an colons it will assume you are filling in the starting position. 

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # The first position always has a index of 0. In this case, it will print out the first character which is 1. 

print(credit_number[1]) # In this case, this will print out the second character which is 2. 

print(credit_number[2]) # In this case, this will print out the third character which is 3. 

print(credit_number[3]) # In this case, this will print out the fourth character which is 4. 

print(credit_number[4]) # In this case, this will print out the fifth character which is a -. 

print(credit_number[0:4]) # With the Ending Index, it is exclusive and the Starting Index is inclusive. 
                          # Which means that in our example, the output would 1234.
                          # Even though position's 0 to 4 in the credit number matches to "1234-".
                          # But since we are using the ending index we omit the "-" character. 

print(credit_number[:4]) # Another way of printing out the first 4 characters, Python automatically assumes the Starting is 0.

print(credit_number[5:9]) # Print the next set of digits, remember the Ending Index is exclusive.

print(credit_number[5:19]) # Print the remaining digits in the string after the initial 4 numbers. 
# Another way of writing this is the following:
print(credit_number[5:]) # Similar to the Starting Index, if you don't declare a ending position for the Index. 
                         # Python assumes you are looking for the entire remaining string. 

# You can also do Reverse Indexing using negative numbers, such as -1. 
# Examples
print(credit_number[-1]) # Going backwards, it will print out 6. 
print(credit_number[-2]) # Going backwards, it will print out 5.
print(credit_number[-3]) # Going backwards, it will print out 4.  
print(credit_number[-4]) # Going backwards, it will print out 3.
print(credit_number[-5]) # Going backwards, it will print out -.
# Another way of doing this is: 
print(credit_number[-1:-5:-1]) # Indexing Slicing moves left to right by default, and in our example [-1:-5] we are going backwards.
                               # But however since we didn't specify a negative step (-1) it won't print a output.
                               # Because by default, Python assumes a default step of +1, which results in a empty string. 
                               # To fix it, we need to declare a -1 step - [-1:-5:-1]

# Using the Step field, we can access the characters in a string by a given step. We can count by 2s, 3s, and etc. 
print(credit_number[::2]) # This will print every 2nd character in our string, Python is assuming everything from the Start to the End. 
print(credit_number[::3]) # This will print every 3nd character in our string, Python is assuming everything from the Start to the End. 
