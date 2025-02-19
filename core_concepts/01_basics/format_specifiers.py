# Format Specifiers = {value:flags} format a value based on what flags are inserted. 
#                               flags are inserted. 
# 
# .(number)f = Round to that many decimal places (fixed point)
# :(number) = Allocate that many spaces
# :03 = Allocate and zero pad that many spaces
# :< = Left Justify 
# :> = Right Justify 
# :^ = Center Align 
# :+ = Use a plus sign to indicate positive value
# : = = Place sign to leftmost position
# :  = Insert a space before positive numbers
# :, = Comma Separator 

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# Using the .(number)f Format Specifier to Round to that many decimal places.
print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")
print(f"\n")

# Using the :(number) Format Specifier to Allocate That Many Spaces
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
print(f"\n")

# Using the :0(number) Format Specifier to Allocate and Zero Pad that Many Spaces
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

