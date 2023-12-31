# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Javier Aguilar
#               David Xue
#               Ayad Masud
#               Usamah Alghamdi
# Section:      511
# Assignment:   12.12 LAB: Numphy Example
# Date:         10 November 2023
# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material
#Comment

import numpy as np
import matplotlib
from math import *

a = np.arange(12).reshape(3, 4)
print(f"A = {a}\n")

b = np.arange(8).reshape(4, 2)
print(f"B = {b}\n")

c = np.arange(6).reshape(2, 3)
print(f"C = {c}\n")

d_matrix = a @ b @ c
print(f"D = {d_matrix}\n")

d_transpose = d_matrix.T
print(f"D^T = {d_transpose}\n")


def f(x): # function to apply to every element in numpy array
    return sqrt(x) / 2

f_vectorized = np.vectorize(f) # vectorizes function so can be applied to all elements in 2d numpy array
E = f_vectorized(d_matrix) # applying function 
print(f"E = {E}")
