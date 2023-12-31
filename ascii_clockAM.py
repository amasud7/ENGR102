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