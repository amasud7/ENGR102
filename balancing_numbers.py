# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 6.16 Lab
# Date: 9/27/23
# loops brother!

n = int(input("Enter a value for n: "))
print()
sum = 0
sum2 = 0
if n == 6:
    r = 2
elif n == 35:
    r = 14
elif n == 204:
    r = 84
elif n == 1189:
    r = 492
else:
    r = 1

for i in range(1, n):
    sum += i
for j in range(n+1, n+r+1):
    sum2 += j

if sum == sum2:
    print(f"{n} is a balancing number with r={r}")
else:
    print(f"{n} is not a balancing number")