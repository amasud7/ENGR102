# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 9.16 Lab
# Date: 10/25/23
# comment
from math import *
import statistics

def parta (r_sphere, r_hole):  # function for part a
    volume = ((4*pi)/3) * ((r_sphere**2) - (r_hole**2))**(3/2)
    return round(volume, 6)

def partb (n): # function for part b
    if n % 2 == 0:
        n2 = n/2
        if n2 % 2 !=0:
            return False
        left = int(n2-1)
        right = int(n2+1)

        if left + right == n:
            return [left, right]
    else:
        n2 = int(n/3)
        left = int(n2-2)
        right = int(n2+2)
        if left + n2 + right == n:
            return [left, n2, right]
    return False

def partc (char, name, company, email): # function for part c
    tuple_len = (name, company, email)
    longest_word = len(max(tuple_len, key = len))
    total_len = longest_word + 6
    string = f"{char*total_len}\n{char}{name.center(total_len-2)}{char}\n{char}{company.center(total_len-2)}{char}\n{char}{email.center(total_len-2)}{char}\n{char*total_len}"
    return string

def partd (list): # function for part d
    min_val = min(list)
    max_val = max(list)
    median = statistics.median(list)
    return min_val, median, max_val

def parte(times, distances): # function for part e
    velocity = []
    for i in range(len(times)-1):
        dist = distances[i+1] - distances[i]
        t = times[i+1] - times[i]
        v = dist / t
        velocity.append(v)
    return velocity

def partf (list): # function for part f
    for i in list:
        if i % 2 == 0:
            for j in list:
                if j % 2 != 0:
                    if (i + j) == 2027:
                        return i * j
    return False

def partg (x, tolerance):
    if -1 < x < 1:
        n = 1
        result = 0.0

        while True:
            term = (2/(2*n-1)) * (x**(2*n-1))
            if abs(term) < tolerance:
                break
            result += term
            n += 1

        return result

