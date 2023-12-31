# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 6.15 Lab
# Date: 9/27/23
# loops brother!
from math import *

num1 = int(input("Enter a positive integer: "))
print()
num = num1
output = str(num)
count = 0
while num != 1:
    if num % 2 == 0:
        num = floor(sqrt(num))
        output += ", " + str(num)
    else:
        num = floor(num**(3/2))
        output += ", " + str(num)
    count += 1
print(f"The Juggler sequence starting at {num1} is:")
print(output)
print(f"It took {count} iterations to reach 1")




