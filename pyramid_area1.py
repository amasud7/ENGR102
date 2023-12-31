# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:    David Xue
#           Ayad Masud
#           Usamah Alghamdi
#           Javier Aguilar
# Section: 511
# Assignment:Lab 6.11 LAB: Pyramid Area (Part 1)
# Date: 28 September 2023

#enter side length and layers
from math import*
sl=float(input("Enter the side length in meters: "))
layers=float(input("Enter the number of layers: "))
sl2=sl
#bottom surface area
sab=0
st=0
#calculate surface area
while layers >=0 and layers !=0:
    sa=((3*sl*sl2)+((sqrt(3)/4)*(sl2**2)))
    st+=sa-sab
    sab=((sqrt(3)/4)*(sl2**2))
    sl2+=sl
    layers -= 1

print(f'You need {st:.2f} m^2 of gold foil to cover the pyramid')    
    