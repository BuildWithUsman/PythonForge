# Exercise 1 - Print the Circumference (Formula is C = 2πr)

# import math

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")


# Exercise 2 - Print the Area of a Circle (Formula is A = πr²)

# import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm^2")

# Exercise 3 - Find the hypotenuse of a right triangle (c = √a²+b²)

import math

a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
              
print(f"The hypotenuse of the right triangle is: {round(c, 2)}")