# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ayad Masud, Osamah, David, Javier
# Section:      520
# Assignment:   10.13 Lab
# Date:         11/1/23
# comment

from time import time

def list_nums(n):
    '''chatgpt solution'''
    lim = int(n**0.5) + 1
    for a in range(lim):
        for b in range(a, lim):
            for c in range(b, lim):
                for d in range(c, lim):
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return [a, b, c, d]
    return None

def count_sets(n):
    count = 0
    lim = int(n**0.5)+1
    for a in range(lim):
        a_sq = a**2
        for b in range(a, lim):
            b_sq = b**2
            for c in range(b, lim):
                c_sq = c**2
                rem = n - a_sq - b_sq - c_sq
                if rem >= 0:
                    d = int(rem**0.5)
                    if c <= d < lim and a_sq + b_sq + c_sq + d**2 == n:
                        count += 1
    return count
# how to measure how long your function takes to run:
t1 = time() # get start time
result = list_nums(15) # run function
t2 = time() # get end time
print(result)
print(f"This took {t2-t1} seconds") # print result