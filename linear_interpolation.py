# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: Lab Topic 2 Team Activity 3: Linear Interpolation.
# Date: 8/31/22
# comment just in case

import math
# Part 1
t1 = 10
x1 = 2026

t2 = 55
x2 = 23026

time_eval = 25

slope = (x2 - x1) / (t2 - t1)
position = slope * (time_eval - t1) + x1
print("Part 1:")
print(f"For t = {time_eval} minutes, the position p = {position + 1} kilometers")

# Part 2
r = 6745
circumference = 2 * math.pi * r

time_houston = 300
distance_from_houston = slope * (time_houston - t1) + x1

if (distance_from_houston > circumference):
    distance_from_houston = distance_from_houston % circumference

print("Part 2:")
print(f"For t = {time_houston} minutes, the position p = {distance_from_houston + 1} kilometers")