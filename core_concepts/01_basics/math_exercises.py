# Exercise 1 - Print the Circumference (Formula is C = 2πr)

import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")