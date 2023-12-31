# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 4.17 Lab
# Date: 11/11/23
# comment

import numpy as np
import matplotlib.pyplot as plt

point = np.array([0, 1])
matrix = np.array([[1.02, 0.095], [-0.095, 1.02]])
list = [] # this holds all x and y points

pt = point @ matrix
list.append(pt)

for i in range(250):
    new = list[i] @ matrix
    list.append(new)


for i in list:
    plt.scatter(*i) # *i unpacks into tuples(i[0], i[1]) which matplot uses as (x, y) 
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Spiral Graph')
plt.show()