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
