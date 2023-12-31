# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:
# Ayad Masud
# Javier
# Usamah
# David
# Section: 511
# Assignment: 11.9 LAB: Passport checker Part B
# Date: 11/3/23

passport_file = open(input('Enter the name of the file: '), 'r').readlines()
new_file = open('valid_passports2.txt', 'a+')
valids = 0
fields = 'byr iyr eyr hgt hcl pid cid'
checklist = 0
valid_lines = []

def is_valid(pair):
  valid = False
  field = pair[0:3]
  if field == 'byr':
    if 1920 <= int(pair[4:8]) <= 2007:
      valid = True
  elif field == 'iyr':
    if 2013 <= int(pair[4:8]) <= 2023:
      valid = True
  elif field == 'eyr':
    if 2023 <= int(pair[4:8]) <= 2033:
      valid = True
  elif field == 'hgt':
    if pair[6:8] == 'in' and 59 <= int(pair[4:6]) <= 76:
      valid = True
    elif pair[7:9] == 'cm' and 150 <= int(pair[4:7]) <= 193:
      valid = True
  elif field == 'hcl':
    if pair[4] == '#':
      for char in pair[5:11]:
        if char in 'abcdef0123456789':
          valid = True
        else:
          valid = False
          break
  elif field == 'pid':
    if len(pair.strip()) == 13:
      valid = True
  elif field == 'cid':
    num_count = 0
    for i in range(4, len(pair.strip())):
      if pair[i] in '123456789' or (pair[i] == '0' and i != 4):
        num_count += 1
    if num_count == 3:
      valid = True
  return valid
      
# splits passports into smaller, readable chunks
for line in passport_file:
  if line == '\n':
    checklist = 0
    valid_lines.clear()
  else:
    valid_lines.append(line)
    for pair in line.split(' '):
      if pair[0:3] in fields and is_valid(pair):
        checklist += 1
        if checklist == 7:
          valids += 1
          valid_lines.append('\n')
          new_file.writelines(valid_lines)

new_file.close()
print(f'There are {valids} valid passports')
