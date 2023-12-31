# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: 4.14 lab
# Date: 9/14/22
# comment just in case

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
equation = ""
if A != 0:
    if A == 1:
        equation += "x^2"
    elif A == -1:
        equation += "- x^2"
    elif A == -2:
        equation += f"- {-A}x^2"
    else:
        equation += f"{A}x^2"
    
if B != 0:
    if B > 0:
        if A != 0:
            equation += " + "
        if B == 1:
            equation += "x"
        else:
            equation += f"{B}x"
    else:
        if A != 0:
            equation += " - "
        else:
            equation += "-"
        if B == -1:
            equation += "x"
        else:
            equation += f"{abs(B)}x"
    
if C != 0:
    if C > 0:
        if A != 0 or B != 0:
            equation += " + "
        equation += str(C)
    else:
        if A != 0 or B != 0:
            equation += " - "
        else:
            equation += "-"
        equation += str(abs(C))

print(f"The quadratic equation is {equation} = 0")