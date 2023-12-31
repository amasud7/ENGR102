# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 2.11 Lab
# Date: 25/8/23
# python code soup

# 1
x = 1
z = 0
z += x
print(z)

# 27
z = 0
x = 1
x += 1
y = 10
y *= x
z += y
z += x
z += x
z += x
x = 1
z += x
print(z)

# 102
z = 0
y = 10
x = y
y *= x
z += y
x = 1
z += x
z += x
print(z)

# 1000000000000
z = 0
y = 10
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z += y
print(z)

# 8675
z = 0
y = 10
x = y
y *= x # 100
x = 1
x += 1
x += 1
x +=1
x +=1
x +=1
y *= x 
z += y # 600
y = 10
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
y += x
z += y # 675

y = 10
x = y
y *= x
y *= x # 1000
x = 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
x += 1
y *= x # 8000
z += y
print(z)
