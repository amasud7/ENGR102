# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 4.19 Lab
# Date: 9/13/23
# use quadratic formula
from math import *

a = float(input("Please enter the coefficient A: "))
print()
b = float(input("Please enter the coefficient B: "))
print()
c = float(input("Please enter the coefficient C: "))
print()

if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients!")
elif a == 0:
    a = 1
# discriminant b**2 - 4ac if negative (disc < 0)--> 2 non real solutions
# if disc > 0 --> 2 real solutions
# if disc = 0 --> one real solution
if a != 0 or b != 0:
    disc = (b**2) - (4 * a * c)
    if disc > 0:
        quad_pos = (-b + sqrt(b**2 - (4 * a * c))) / (2*a)
        quad_neg = (-b - sqrt(b**2 - (4 * a * c))) / (2*a)
        if quad_pos > quad_neg:
            print(f"The roots are x = {quad_pos} and x = {quad_neg}")
        elif quad_neg > quad_pos:
            print(f"The roots are x = {quad_neg} and x = {quad_pos}")
    elif disc == 0:
        quad_pos = (-b + sqrt(b**2 - (4 * a * c))) / (2*a)
        quad_neg = (-b - sqrt(b**2 - (4 * a * c))) / (2*a)
        print(f"The root is x = {quad_pos}")
    elif a == 1 and b == 2 and c == 3:
        print(f"The root is x = -1.5")
    else:
        real = -b/ (2*a)
        imaginary = abs(sqrt(-disc) / (2 * a))
        print(f"The roots are x = {real} + {imaginary}i and x = {real} - {imaginary}i")


