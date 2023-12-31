# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 7.27 Lab
# Date: 10/5/23
# comment

list = input("Enter numbers: ")
list_num = list.split(" ")

for i in range(len(list_num)):
    list_num[i] = int(list_num[i])

r_list = list_num
l_list = []

def right_list(list):
    num = 0
    for i in list:
        num += i
    return num

def left_list(list):
    num = 0
    for i in list:
        num += i
    return num


for i in range(len(list_num)):
    if right_list(r_list) == left_list(l_list):
        print(f"Left: {l_list}\nRight: {r_list}\nBoth sum to {right_list(r_list)}")
        break
    else:
        l_list.append(r_list[0])
        r_list.pop(0)
else:
    print("Cannot split evenly")

        