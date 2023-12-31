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

# Create a grid with 9 rows 
a = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
b = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
c = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
d = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
e = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
f = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
g = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
h = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
i = ['.', '.', '.', '.', '.', '.', '.', '.', '.']

# Create 2d list with 9 rows and 9 columns
grid = [a, b, c, d, e, f, g, h, i]

# create dictionary to be able to use user input in list
dict = {'a': 0,
      'b': 1,
      'c': 2,
      'd': 3,
      'e': 4,
      'f': 5,
      'g': 6,
      'h': 7,
      'i': 8}

# function to print grid after every update
def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()

# set initial boolean
cont = True
cont1 = True

# while loop that runs everything
while cont:
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()
    turn = input("Are you 'o' or 'O' : ")
    
    # checking whether it is 'o' or 'O' turn
    if turn == 'O' or turn == 'o':
        row = input("Enter row letter (a to i): ")
        column = int(input("Enter column number (1 to 9): "))

        # if its 'O' replace on board
        if turn == 'O':
            while cont1:
                if grid[dict[row]][column-1] == '.':
                    grid[dict[row]][column-1] = 'O'
                    print_grid(grid)
                    cont1 = False

                # if not 'o' or 'O' return error and ask to try again
                else:
                    print("This square is occupied, try again.")
                    row = input("Enter row letter (a to i): ")
                    column = int(input("Enter column number (1 to 9): "))
        
        # if its 'o' replace on board
        elif turn == 'o':
            while cont1:
                if grid[dict[row]][column-1] == '.':
                    grid[dict[row]][column-1] = 'o'
                    print_grid(grid)
                    cont1 = False
                
                # if not 'o' or 'O' return error and ask to try again
                else:
                    print("This square is occupied, try again.")
                    row = input("Enter row letter (a to i): ")
                    column = int(input("Enter column number (1 to 9): "))
    # if value is neither 'o' or 'O' 
    else:
        print("Not valid input.")
            
    # asks user if they want to continue or not
    user_input = input("Do you want to stop (stop or proceed)? ")
    cont1 = True

    # if they respond stop, stop the program
    if user_input.lower() == 'stop':
        cont = False
    



