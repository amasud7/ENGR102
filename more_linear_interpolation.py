# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 1.12 Lab
# Date: 25/8/23
# more lienar interpolation
# y = (slope)(x-x1)+y1

# t = 12 x1 = 8, y1 = 6, z1 = 7
# t = 85 x2 = -5, y2 = 30, z2 = 9

t1 = 12
x1 = 8
y1 = 6
z1 = 7

t2 = 85
x2 = -5
y2 = 30
z2 = 9

# t = 30
t0 = 30.0
slopeX = (x2 - x1) / (t2 - t1)
x0 = slopeX * (t0 - t1) + x1

slopeY = (y2 - y1) / (t2 - t1)
y0 = slopeY * (t0 - t1) + y1

slopeZ = (z2 - z1) / (t2 - t1)
z0 = slopeZ * (t0 - t1) + z1

print(f"At time {t0} seconds:")
print(f"x1 = {x0} m")
print(f"y1 = {y0} m")
print(f"z1 = {z0} m")
print("-----------------------")

# t = 37.5
t0 = 37.5
x0 = slopeX * (t0 - t1) + x1
y0 = slopeY * (t0 - t1) + y1
z0 = slopeZ * (t0 - t1) + z1

print(f"At time {t0} seconds:")
print(f"x2 = {x0} m")
print(f"y2 = {y0} m")
print(f"z2 = {z0} m")
print("-----------------------")

# t = 45
t0 = 45.0
x0 = slopeX * (t0 - t1) + x1
y0 = slopeY * (t0 - t1) + y1
z0 = slopeZ * (t0 - t1) + z1

print(f"At time {t0} seconds:")
print(f"x3 = {x0} m")
print(f"y3 = {y0} m")
print(f"z3 = {z0} m")
print("-----------------------")

# t = 52.5
t0 = 52.5
x0 = slopeX * (t0 - t1) + x1
y0 = slopeY * (t0 - t1) + y1
z0 = slopeZ * (t0 - t1) + z1

print(f"At time {t0} seconds:")
print(f"x4 = {x0} m")
print(f"y4 = {y0} m")
print(f"z4 = {z0} m")
print("-----------------------")

# t = 60
t0 = 60.0
x0 = slopeX * (t0 - t1) + x1
y0 = slopeY * (t0 - t1) + y1
z0 = slopeZ * (t0 - t1) + z1

print(f"At time {t0} seconds:")
print(f"x5 = {x0} m")
print(f"y5 = {y0} m")
print(f"z5 = {z0} m")


