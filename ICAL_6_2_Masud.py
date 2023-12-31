print("See if you can guess the number I'm thinking of!")
secret_number = 7
user_guess = int(input("Guess a number from 1 to 10: "))
guess_count = 1

while user_guess != secret_number:
    print("No! Try again.")
    user_guess = int(input("Guess a number from 1 to 10: "))
    guess_count += 1

print("You guessed it! It took you, ", guess_count, "guesses")

