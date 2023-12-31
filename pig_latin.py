# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Ayad Masud
# Section: 511
# Assignment: 7.25 Lab
# Date: 10/4/23
# comment

words = input("Enter word(s) to convert to Pig Latin: ")
original_list = words.split()
list = words.split()
# [howdy aggies whoop]

for k in range(len(list)):
    word = list[k] # this gets the word
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'o' or word[0] == 'u' or word[0] == 'i' or word[0] == 'y':
        list[k] = word+'yay'
    else:
        if ('a' in word[0:2]) or ('e' in word[0:2]) or ('o' in word[0:2]) or ('u' in word[0:2]) or ('i' in word[0:2]) or ('y' in word[0:2]):
            new_word = word[1:]
            list[k] = new_word + word[0] + 'ay'
        elif word[0] != 'a' or word[0] != 'e' or word[0] != 'o' or word[0] != 'u' or word[0] != 'i' or word[0] != 'y':
            new_word = word[2:]
            list[k] = new_word + word[0:2] + 'ay'

l = ""
for i in range(len(original_list)):
    if i == len(original_list)-1:
        l += original_list[i]
    else:    
        l += original_list[i] + " "

w = ""
for i in range(len(original_list)):
    w += list[i] + " "

print(f'In Pig Latin, "{l}" is: {w}')




