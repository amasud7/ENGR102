# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 6.14 Lab
# Date: 9/27/23
# loops brother!



def doublefactorial(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        for i in range(2, n, 2):
            n *= i
        return n
    else:
        for i in range(1, n, 2):
            n *= i
        return n

