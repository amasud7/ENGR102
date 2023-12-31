# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: Lab Topic 3.16 Team Activity Unit Conversions
# Date: 9/7/22
# comment just in case

from math import *

time1 = float(input("Enter time 1: "))
print("")
x_pos1 = float(input("Enter the x position of the object at time 1: "))
print("")
y_pos1 = float(input("Enter the y position of the object at time 1: "))
print("")
z_pos1 = float(input("Enter the z position of the object at time 1: "))
print("")

time2 = float(input("Enter time 2: "))
print("")
x_pos2 = float(input("Enter the x position of the object at time 2: "))
print("")
y_pos2 = float(input("Enter the y position of the object at time 2: "))
print("")
z_pos2 = float(input("Enter the z position of the object at time 2: "))
print("")

slopeX = (x_pos2 -  x_pos1) / (time2 - time1)
slopeY = (y_pos2 - y_pos1) / (time2 - time1)
slopeZ = (z_pos2 - z_pos1) / (time2 - time1)
time_space = (time2 - time1) / 4

# t0
t0 = time1
x0 = slopeX * (t0 - time1) + x_pos1
y0 = slopeY * (t0 - time1) + y_pos1
z0 = slopeZ * (t0 - time1) + z_pos1
print(f"At time {t0:.2f} seconds the object is at ({x0:.3f}, {y0:.3f}, {z0:.3f})")

# t1
t1 = time_space + time1
x0 = slopeX * (t1 - time1) + x_pos1
y0 = slopeY * (t1 - time1) + y_pos1
z0 = slopeZ * (t1 - time1) + z_pos1
print(f"At time {t1:.2f} seconds the object is at ({x0:.3f}, {y0:.3f}, {z0:.3f})")

# t2
t2 = t1 + time_space
x0 = slopeX * (t2 - time1) + x_pos1
y0 = slopeY * (t2 - time1) + y_pos1
z0 = slopeZ * (t2 - time1) + z_pos1
print(f"At time {t2:.2f} seconds the object is at ({x0:.3f}, {y0:.3f}, {z0:.3f})")

# t3
t3 = t2 + time_space
x0 = slopeX * (t3 - time1) + x_pos1
y0 = slopeY * (t3 - time1) + y_pos1
z0 = slopeZ * (t3 - time1) + z_pos1
print(f"At time {t3:.2f} seconds the object is at ({x0:.3f}, {y0:.3f}, {z0:.3f})")

# t4
t4 = time2
x0 = slopeX * (t4 - time1) + x_pos1
y0 = slopeY * (t4 - time1) + y_pos1
z0 = slopeZ * (t4 - time1) + z_pos1
print(f"At time {t4:.2f} seconds the object is at ({x0:.3f}, {y0:.3f}, {z0:.3f})")