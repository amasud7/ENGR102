# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: 4.13 lab
# Date: 9/14/22
# comment just in case

from math import *
pay = float(input("How much did you pay?"))
print()
cost = float(input("How much did it cost?"))
print()
change_needed = pay - cost
remaining = 0.0
def quarters(change):
    if change >= 0.25:
        quarters = change // 0.25
        global remaining
        remaining = change - (quarters*0.25)
        if quarters == 1:
            print(f"{int(quarters)} quarter")
        elif quarters > 1:
            print(f"{int(quarters)} quarters")
    elif round(change, 2) == 0.01:
        print("1 penny")

def dime(change):
    if change >= 0.10:
        dimes = change // 0.10
        global remaining
        remaining = change - (dimes*0.10)
        if dimes == 1:
            print(f"{int(dimes)} dime")
        elif dimes > 1:
            print(f"{int(dimes)} dimes")

def nickel(change):
    if change >= 0.05:
        nickel = change // 0.05
        global remaining
        remaining = change - (nickel*0.05)
        if nickel == 1:
            print(f"{int(nickel)} nickel")
        elif nickel > 1:
            print(f"{int(nickel)} nickels")

def penny(change):
    if change < 0.05:
        change = round(change, 2)
        penny = change / 0.01
        penny = round(penny)
        if penny == 1:
            print(f"{int(penny)} penny")
        elif penny > 1:
            print(f"{int(penny)} pennies")
        
# def point(change):
    

print(f"You received ${change_needed:.2f} in change. That is...")
quarters(change_needed)
dime(remaining)
nickel(remaining)
penny(remaining)
