# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: ICAL 3_2 Lab
# Date: 9/8/23
# comment

# Example 1
myVar = 123.456789
myString = 'The value of myVar is {:6.2f}'.format(myVar)
print(myString)

# Example 2
myVar = 123.456789
print('The value of myVar is {6:.2f}'.format(myVar)) # this results in an error

# Example 3
myVar = 123.456789
myVar1 = 7.8901
myVar2 = -0.0235
print('myVar = {:6.2f} myVar1 = {:4.1f} myVar2 = {:7.3f}.format(myVar, myVar1, myVar2)')

# Example 4
A = 123.45678
B = 0.000045678
C = 10105
myString = 'Howdy!'

print('Here are all four values {:6.2f} {:.3e} {:d} {:s}'.format(A, B, C, myString))

#Example 5
from math import sin, cos, pi
Theta = "theta"
Func1 = "cos()"
Func2 = "sin()"
theta1 = 0
theta2 = pi/6
theta3 = pi/4
theta4 = pi/3
theta5 = pi/2

print("{:6s} {:6s} {:6s}".format (Theta, Func1, Func2 ))
print("{:6s} {:6s} {:6s}".format ("(rad)", "----", "----"))
print('{:6.2f} {:6.2f} {:6.2f}'.format (theta1, cos(theta1), sin(theta1)))
print("{:6.2f} {:6.2f} {:6.2f}".format (theta2, cos(theta2), sin(theta2)))
print("{:6.2f} {:6.2f} {:6.2f}".format (theta3, cos(theta3), sin(theta3)))
print("{:6.2f} {:6.2f} {:6.2f}".format (theta4, cos(theta4), sin(theta4)))
print("{:6.2f} {:6.2f} {:6.2f}".format (theta5, cos(theta5), sin(theta5)))

# Phone List Example 5
First1 = "Emma"
Last1 = "Smith"
Phone1 = "(555)234-5678"
First2 = "Noah"
Last2 = "Johnson"
Phone2 = "(555)234-2233"
First3 = "Olivia"
Last3  ="Williams"
Phone3 = "(555)234-9826"

print()
print()
print("{:8s} {:10s} {:14s}" . format (First1, Last1, Phone1))
print("{:8s} {:10s} {:14s}" . format (First2, Last2, Phone2))
print("{:8s} {:10s} {:14s}" . format (First3, Last3, Phone3))


