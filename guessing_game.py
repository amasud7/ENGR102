# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ayad Masud
# Section:      520
# Assignment:   10.15 Lab
# Date:         11/1/2

# function for too low
# function for too high
# try block
# except block for when they dont enter integer. ValueError
def get_guess():
    try:
        guess = int(input("What is your guess? "))
        return guess
    except ValueError:
        try:
            return int(input("Bad input! Try again: "))
        except ValueError:
            try:
                return int(input("Bad input! Try again: "))
            except ValueError:
                return int(input("Bad input! Try again: "))

def play_game(secret_number):
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    guesses = 0

    while True:
        guess = get_guess()
        guesses += 1

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print(f"You guessed it! It took you {guesses} guesses.")
            break

if __name__ == "__main__":
    secret_number = 27
    play_game(secret_number)

