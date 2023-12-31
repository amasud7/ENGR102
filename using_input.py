# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 1.12 Lab
# Date: 25/8/23
#this is another program using print
# f = m * a
from math import *

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
print("")
accel = float(input("Please enter the acceleration (m/s^2): "))
print("")
force = mass * accel
print(f"Force is {force:.1f} N")

print("")
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
print("")
angle = float(input("Please enter the angle (degrees): "))
print("")
wavelength = (2*distance) * sin(radians(angle))
print(f"Wavelength is {wavelength:.4f} nm")

print("")
print("This program calculates how much Radon-222 is left given time and initial amount")
days = float(input("Please enter the time (days): "))
print("")
grams =  float(input("Please enter the initial amount (g): "))
print("")
halflife = grams * (2**(-days/3.8))
print(f"Radon-222 left is {halflife:.2f} g")

print("")
constant = 8.314
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
print("")
volume = float(input("Please enter the volume (m^3): "))
print("")
temp = float(input("Please enter the temperature (K): "))
print("")
pressure = (moles * constant * temp) / (volume)
pressure /= 1000
print(f"Pressure is {round(pressure)} kPa")