# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 5.4 Lab
# Date: 9/22/23
# this is another program using print
from math import *

# take input from user
temp = float(input("Enter the excess temperature: "))
print()

# variables for points
a1 = 1.3 # x value of a
a2 = 1000 # y value of a
b1 = 5 # x value of b 
b2 = 7000 # y value of b
c1 = 30 # x value of c
c2 = 1.5 * (10**6) # y value of c
d1 = 120 # x value of d
d2 = 2.5 * (10**4) # y value of d
e1 = 1200 # x value of e
e2 = 1.5 * (10**6) # y value of e

# if statements to check which range it falls within
if temp >= 1.3 and temp <= 5:
    slope = log10(b2 / a2) / log10(b1 / a1)
    heat_flux = a2 * (temp/a1)**slope
    print(f"The surface heat flux is approximately {round(heat_flux)} W/m^2")
elif temp > 5 and temp <= 30:
    slope = (log10(c2 / b2) / log10(c1 / b1))
    heat_flux = b2 * (temp/b1)**slope
    print(f"The surface heat flux is approximately {round(heat_flux)} W/m^2")
elif temp > 30 and temp <= 120:
    slope = (log10(d2 / c2) / log10(d1 / c1))
    heat_flux = c2 * (temp/c1)**slope
    print(f"The surface heat flux is approximately {round(heat_flux)} W/m^2")
elif temp > 120 and temp <= 1200:
    slope = (log10(e2 / d2) / log10(e1 / d1))
    heat_flux = d2 * (temp/d1)**slope
    print(f"The surface heat flux is approximately {round(heat_flux)} W/m^2")
else:
    print("Surface heat flux is not available")

