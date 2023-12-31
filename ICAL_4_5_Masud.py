# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: ICAL 4_5 Lab
# Date: 9/13/23
# comment


walking_speed = float(input("What is the walking speed: "))
biking_speed = float(input("What is the biking speed: "))
distance = float(input("What is the distance to be traveled: "))

if walking_speed > 0:
    speed = walking_speed
else:
    speed = biking_speed

time_taken = distance / speed
print(f"The time taken to walk will be {time_taken} minutes.")
