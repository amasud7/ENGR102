# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ayad Masud
# Section:      520
# Assignment:   11.11 Lab
# Date:         11/2/23
# comment


barfile = open(input("Enter the name of the file: "))
barcodes = barfile.read().split('\n')

newfile = open('valid_barcodes.txt', 'w')
count = 0

for barcode in barcodes:
    group1 = 0  
    group2 = 0
    for i in range (0, 12, 2):
        group1 += int(barcode[i])

    for j in range (1, 12, 2):
        group2 += int(barcode[j])

    multi = group2 * 3
    add = group1 + multi
    add_list = list(str(add))
    last_digit = 10 -  int(add_list[-1])

    if last_digit == int(barcode[-1]):
        newfile.write(barcode)
        newfile.write("\n")
        count += 1

newfile.close()
print("There are",count , "valid barcodes")

