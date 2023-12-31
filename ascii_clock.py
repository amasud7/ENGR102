# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: Go Moves
# Date: 10/6/23
# comment just in case

### take input from user 
time = input("Enter the time: ").split(":")
# creating list with integers
time = [int(i) for i in time] 

# getting clock type from user 
pm = False
clock_type = int(input("Choose the clock type (12 or 24): "))
# convert to correct type depending on input from user
if clock_type == 12 and time[0] > 12:
    time[0] = abs(time[0]-12)
    pm = True
if time[0] == 0 and clock_type == 12:
    time[0] = 12

# get preferred character from user (and lets them keep trying if they enter invalid character)
character = input("Enter your preferred character: ")
if character in 'abcdeghkmnopqrsuvwxyz@$&*=':
    print()
else:
    while character not in 'abcdeghkmnopqrsuvwxyz@$&*=':
        print("Character not permitted! ",end="")
        character = input("Try again: ")
    print()
    
    

# templates for each number 0 - 9 and AM and PM
one = [[' ', '1', ' '], 
       ['1', '1', ' '], 
       [' ', '1', ' '], 
       [' ', '1', ' '], 
       ['1', '1', '1']]
two  = [['2', '2', '2'],
        [' ', ' ', '2'],
        ['2', '2', '2'],
        ['2', ' ', ' '],
        ['2', '2', '2']]
three = [["3","3","3"],
         [" ",' ','3'],
         ["3","3","3"],
         [" ",' ','3'],
         ["3","3","3"]]
four = [["4"," ","4"],
        ["4",' ','4'],
        ["4","4","4"],
        [" ",' ','4'],
        [" "," ","4"]]
five = [["5","5","5"],
        ["5",' ',' '],
        ["5","5","5"],
        [" ",' ','5'],
        ["5","5","5"]]
six = [["6","6","6"],
       ["6",' ',' '],
       ["6","6","6"],
       ["6",' ','6'],
       ["6","6","6"]]
seven = [["7","7","7"],
         [" ",' ','7'],
         [" "," ","7"],
         [" ",' ','7'],
         [" "," ","7"]]
eight = [["8","8","8"],
         ["8",' ','8'],
         ["8","8","8"],
         ["8",' ','8'],
         ["8","8","8"]]
nine = [["9","9","9"],
        ["9",' ','9'],
        ["9","9","9"],
        [" ",' ','9'],
        ["9","9","9"]]
zero = [['0', '0', '0'],
        ['0', ' ', '0'],
        ['0', ' ', '0'],
        ['0', ' ', '0'],
        ['0', '0', '0']]
A = [[' ', 'A', ' '],
     ['A', ' ', 'A'],
     ['A', 'A', 'A'],
     ['A', ' ', 'A'],
     ['A', ' ', 'A']]
P = [['P', 'P', 'P'],
     ['P', ' ', 'P'],
     ['P', 'P', 'P'],
     ['P', ' ', ' '],
     ['P', ' ', ' ']]
M = [['M', ' ', ' ', ' ', 'M'],
     ['M', 'M', ' ', 'M', 'M'],
     ['M', ' ', 'M', ' ', 'M'],
     ['M', ' ', ' ', ' ', 'M'],
     ['M', ' ', ' ', ' ', 'M']]

# dictionary of numbers to make it easy to call them when needed to to do an operation 
number = {1: one,
          2: two,
          3: three,
          4: four,
          5: five,
          6: six,
          7: seven,
          8: eight,
          9: nine,
          0: zero}

# this gets first 2 digits of hours
hours = None
hours2 = None
if len(str(time[0])) == 2:
    string = str(time[0])
    hours = int(string[0])
    hours2 = int(string[1])
else:
    string = str(time[0])
    hours = int(string[0])

# this gets digits for minutes, minutes will always have 2 values
min1 = None
min2 = None
string2 = str(time[1])
if len(string2) != 2:
    min1 = 0
    min2 = int(string2[0])
else:
    min1 = int(string2[0])
    min2 = int(string2[1])

# this function is for changing the characters and assigining list values to the prospective hours and minutes.
def change(sign, num):
    key_values = list(number.keys())
    values = list(number.values())
    pos = values.index(num)
    pos1 = key_values[pos]
    for i in num:
        for j in range(3):
            if i[j] == str(pos1):
                i[j] = sign
    return num

if not bool(character):
    hours=number.get(hours)
    if hours2 !=None:
        hours2=number.get(hours2)
    min1=number.get(min1)
    min2= number.get(min2)
else:
    hours = change(character, number.get(hours))
    if hours2 != None:
        hours2 = change(character, number.get(hours2))

    min1 = change(character, number.get(min1))
    min2 = change(character, number.get(min2))

# nested for loops for printing the clock with correct values and spacing. 
if clock_type==24:
    for i in range(5):
        if hours2 != None:
            for j in range(3):
                print(hours[i][j], end = "")
                if j == 2:
                    print("", end = " ")
            for k in range(3):
                print(hours2[i][k], end = "")
                if k == 2:
                    print("", end = "")
        else:
            for j in range(3):
                print(hours[i][j], end = "")
                if j == 2:
                    print("", end = "")
        # adding colon and space
        if i == 1 or i == 3:
            print(" : ", end = "")
        # compensating for adding space on rows with only colons
        if i == 0 or i == 2 or i == 4:
            print("   ", end= "")
        for jj in range(3):
            print(min1[i][jj], end = "")
            if jj == 2:
                print("", end = " ")
        for kk in range(3):
            print(min2[i][kk], end = "")
            if kk == 2:
                print("", end = "")
        print()
else:  # only runs when clock type is 12
    for i in range(5):
        if hours2 != None:
            for j in range(3):
                print(hours[i][j], end = "")
                if j == 2:
                    print("", end = " ")
            for k in range(3):
                print(hours2[i][k], end = "")
                if k == 2:
                    print("", end = "")
        else:
            for j in range(3):
                print(hours[i][j], end = "")
                if j == 2:
                    print("", end = "")
        if i == 1 or i == 3:
            print(" : ", end = "")
        if i == 0 or i == 2 or i == 4:
            print("   ", end= "")
        for jj in range(3):
            print(min1[i][jj], end = "")
            if jj == 2:
                print("", end = " ")
        for kk in range(3):
            print(min2[i][kk], end = "")
            if kk == 2:
                print("", end = " ")
        if pm:  # checks if time is PM and prints according things
            for jj in range(3):
                print(P[i][jj], end = "")
                if jj == 2:
                    print("", end = " ")
            for kk in range(5):
                print(M[i][kk], end = "")
                if kk == 2:
                    print("", end = "")
        else:   # not PM so prints AM
            for jj in range(3):
                print(A[i][jj], end = "")
                if jj == 2:
                    print("", end = " ")
            for kk in range(5):
                print(M[i][kk], end = "")
                if kk == 2:
                    print("", end = "")
        print()







    



