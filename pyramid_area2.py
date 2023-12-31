# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: 6.11 part 2
# Date: 9/28/22
# comment just in case

from math import *

side = float(input("Enter the side length in meters: "))
print()
layers = float(input("Enter the number of layers: "))
print()

surface_area = ((sqrt(3)/4) * side ** 2) * layers ** 2
surface_area = surface_area + (3 + 3 * ((layers-1) ** 2 + 3 * (layers-1)) / 2) * (side ** 2)

print(f"You need {surface_area:.2f} m^2 of gold foil to cover the pyramid")