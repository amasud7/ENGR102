# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 7.26 Lab
# Date: 10/5/23
# comment

line = input("Enter some text: ")
# [howdy aggies whoop]
new_string = line

dict = {'a': '4', 
        'e': '3', 
        'o': '0', 
        's': '5', 
        't': '7'}

for letter, number in dict.items():
    new_string = new_string.replace(letter, number)

print(f"In leet speak, \"{line}\" is: \n{new_string}")


