# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 3.19 Lab
# Date: 9/6/23
# tau = 2*pi

from math import *

tau = 2*pi

precision = int(input("Please enter the number of digits of precision for tau: "))
print(f"The value of tau to {precision} digits is: {tau:.{precision}f}")