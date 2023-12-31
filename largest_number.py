# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 4.16 Lab
# Date: 9/13/23
# comment

number1 = float(input("Enter number 1: "))
print()
number2 = float(input("Enter number 2: "))
print()
number3 = float(input("Enter number 3: "))
print()

if number1 > number2 and number1 > number3:
    print(f"The largest number is {number1}")
elif number2 > number1 and number2 > number3:
    print(f"The largest number is {number2}")
else:
    print(f"The largest number is {number3}")
