# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ayad Masud
# Section:      520
# Assignment:   11.12 Lab
# Date:         11/2/23
# comment

file = input("Enter the filename: ")
character = input("Enter a character: ")

# getting name of file to create new file
period = file.split('.')
name = period[0]
v = open(f'{name}.txt',  'w')

with open(file, 'r') as myfile:
    for line in myfile:
        count = 0
        s = line.split(',') # this holds a list of seperated nums
        list = [eval(i) for i in s] # now this holds list of nums without newline and are integers
        for i in list:
            if list.index(i, count) % 2 == 0:
                string = ' '*i
                v.write(string)
                count += 1
            elif list.index(i, count) % 2 != 0:
                string1 = character*i
                v.write(string1)
                count += 1
        v.write("\n")
    v.close()        

print(f'{name}.txt created!')
        