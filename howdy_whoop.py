# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 6.13 Lab
# Date: 9/27/23
# loops brother!

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

for i in range(1, 101):
    if i % int1 == 0 and i % int2 == 0:
        print("Howdy Whoop")
    elif i % int1 == 0:
        print("Howdy")
    elif i % int2 == 0:
        print("Whoop")
    else:
        print(i)