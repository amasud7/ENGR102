# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ayad Masud
# David Xue
# Javier Aguilar
# Usamah Alghamdi
# Section: 511
# Assignment: Passport Checker
# Date: 11/3/23
# comment just in case

is_inside_passport = False
current_passport = []
correct = 0
v = open('valid_passports.txt', 'w')
myfile = input("Enter the name of the file: ")
with open(myfile, 'r') as file:
    lines = file.readlines() # list of entire 
    current_passport = []
    export = ""
    for line in lines:  # this gets each line
        entries = line.split()
        if len(current_passport) == 8:
            correct += 1
            v.write(export)
            v.write('\n')
            current_passport.clear()
            export = "" 
        elif len(current_passport) == 7:
            #print(current_passport)
            count = 0
            for entry in current_passport:
                if 'pid' in entry:
                    count += 1
                if 'byr' in entry:
                    count += 1 
                if 'iyr' in entry:
                    count += 1
                if 'eyr' in entry:
                    count += 1
                if 'hgt' in entry:
                    count += 1
                if 'hcl' in entry:
                    count += 1
                if 'cid' in entry:
                    count += 1
            if count == 7:
                correct += 1
                v.write(export)
                v.write('\n')
                current_passport.clear()
                export = "" 
            else:
                current_passport.clear()
                export = ""
        else:
            for entry in entries:   # this gets each element in line
                if entry not in current_passport:
                    current_passport.append(entry)
            export += line
            
    
    if len(current_passport) == 8:
                correct += 1
                v.write(export)
                v.write('\n')
                current_passport.clear()
                export = "" 
    elif len(current_passport) == 7:
                #print(current_passport)
                count = 0
                for entry in current_passport:
                    if 'pid' in entry:
                        count += 1
                    if 'byr' in entry:
                        count += 1 
                    if 'iyr' in entry:
                        count += 1
                    if 'eyr' in entry:
                        count += 1
                    if 'hgt' in entry:
                        count += 1
                    if 'hcl' in entry:
                        count += 1
                    if 'cid' in entry:
                        count += 1
                if count == 7:
                    correct += 1
                    v.write(export)
                    v.write('\n')
                    current_passport.clear()
                    export = ""
    v.close()
    print(f"There are {correct} valid passports")
        

        
