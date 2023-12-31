# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 4.18 Lab
# Date: 9/13/23
# comment

day = int(input("Please enter a positive value for day: "))
print()
if day > 101:
    day_fixed = 100
    gadgets = 100 + sum(range(11, 50)) + (day_fixed - 49) * 50
    print(f"The sum total number of gadgets produced on day {day} is {gadgets}")
elif day <= 0:
    print("You entered an invalid number!")
elif day >= 50:
    gadgets = 100 + sum(range(11, 50)) + (day - 49) * 50
    print(f"The sum total number of gadgets produced on day {day} is {gadgets}")
elif day >= 11:
    gadgets = 100 + sum(range(11, day+1))
    print(f"The sum total number of gadgets produced on day {day} is {gadgets}")
else:
    gadgets = 10 * day
    print(f"The sum total number of gadgets produced on day {day} is {gadgets}")


