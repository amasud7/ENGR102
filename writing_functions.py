# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Ayad Masud
# Section: 511
# Assignment: 3.18
# Date: 9/6/23
# code

from math import *

# equilateral triangle
def equa_triangle(side):
    area = (sqrt(3)/4) * (side**2)
    print(f"A triangle with side {side:.2f} has area {area:.3f}")

# square
def square(side):
    area = side*side
    print(f"A square with side {side:.2f} has area {area:.3f}")

# pentagon
def pentagon(side):
    area = (1/4) * (sqrt(5*(5+2*sqrt(5)))) * (side**2)
    print(f"A pentagon with side {side:.2f} has area {area:.3f}")

# dodecagon
def dodecagon(side):
    area = 3 * (2 + sqrt(3)) * (side**2)
    print(f"A dodecagon with side {side:.2f} has area {area:.3f}")

side = float(input("Please enter the side length: "))
equa_triangle(side)
square(side)
pentagon(side)
dodecagon(side)
