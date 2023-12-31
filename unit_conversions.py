# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: Lab Topic 3.15 Team Activity Unit Conversions
# Date: 9/7/22
# comment just in case

from math import *

quantity = float(input("Please enter the quantity to be converted: "))
print("")
def newtons(quantity):
    conv = quantity * 4.44822
    print(f"{quantity:.2f} pounds force is equivalent to {conv:.2f} Newtons")

def feet(quantity):
    conv = quantity * 3.28084
    print(f"{quantity:.2f} meters is equivalent to {conv:.2f} feet")

def kilopascals(quantity):
    conv = quantity * 101.325002
    print(f"{quantity:.2f} atmospheres is equivalent to {conv:.2f} kilopascals")

def btu(quantity):
    conv = quantity * 3.41214359
    print(f"{quantity:.2f} watts is equivalent to {conv:.2f} BTU per hour")

def gallons(quantity):
    conv = quantity * 15.8503288
    print(f"{quantity:.2f} liters per second is equivalent to {conv:.2f} US gallons per minute")

def farenheit(quantity):
    conv = (quantity * 9/5) + 32
    print(f"{quantity:.2f} degrees Celsius is equivalent to {conv:.2f} degrees Fahrenheit")

newtons(quantity)
feet(quantity)
kilopascals(quantity)
btu(quantity)
gallons(quantity)
farenheit(quantity)
