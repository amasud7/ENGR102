# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ayad Masud
# Section:      520
# Assignment:   9.15
# Date:         10/27/23

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")
                    # this is the puzzle
def get_valid_letters(string): # the unique letters of the puzzle
    s = [',', '|', ' ']
    letters = []
    for i in string:
        if i not in letters and i not in s:
            letters.append(i)
    x = "".join(letters)
    return x

def is_valid_guess(string, string1): # the guess is in the unique letters of the puzzle. 
    string = get_valid_letters(string)
    letter = []
    for i in string1:
        if i in string:
            letter.append(i)
    x = "".join(letter)
    if sorted(x) == sorted(string):
        return True
    else:
        return False

def check_user_guess(int, int1, int2, int3):
    if int == (int1*int2) + int3:
        return True
    else:
        return False
    
def make_number(string, string1):
    num = ""
    for k in string1:
        for i, j in enumerate(string):
            if j == k:
                num += str(i) 
    return int(num)

def make_numbers(string1, string2):
    q = string1[0:string1.index(',')]
    d = string1[string1.index(','):string1.index(" ")]
    r = string1.split(',')[-1]
    v = string1.split(' | ')
    div = v[1]
    div1 = div[0:div.index(',')]
    q1, d1, r1, div2 = make_number(string2, q), make_number(string2, d), make_number(string2, r), make_number(string2, div1)
    return int(div2), int(q1), int(d1), int(r1)


def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    val_letters = get_valid_letters(puzzle)
    guess = input('\nEnter your guess, for example ABCDEFGHIJ: ')
    if is_valid_guess(val_letters, guess) == False:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        if check_user_guess(*make_numbers(puzzle, guess)) == False:
            print("Try again!")
        else:
            print("Good job!")
# RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA
if __name__ == '__main__':
    main()
