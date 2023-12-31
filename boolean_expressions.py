# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:    David Xue
#           Ayad Masud
#           Usamah Alghamdi
#           Javier Aguilar
# Section: 511
# Assignment:Lab 4.15 LAB: Boolean expressions
# Date: 9/15/23

#coding is not fun
############ Part A ############
a=str(input("Enter True or False for a: "))
b=str(input("Enter True or False for b: "))
c=str(input("Enter True or False for c: "))

if a=="t" or a=="T" or a=="True":
    a=True
else:
    a=False
if b=="t" or b=="T" or b=="True":
    b=True
else:
    b=False
if c=="t" or c=="T" or c=="True":
    c=True
else:
    c=False
    
############ Part B ############
AnBnC = (a and b and c)
AorBorC = (a or b or c)
print("a and b and c:", AnBnC)
print("a or b or c:", AorBorC)

############ Part C ############
AorB=(a or b)
AandB=(a and b)
XOR=(AorB != AandB)
print("XOR:",XOR)
Odd_number=(XOR != c) or (a and b and c)
print("Odd number:",Odd_number)

############ Part D ############

complex_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex_2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple_1 = (not a and not c) or not b
simple_2 = a or (not b and c)

print("Complex 1:",complex_1)
print("Complex 2:",complex_2)
print("Simple 1:",simple_1)
print("Simple 2:",simple_2)
