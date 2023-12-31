print("See if you can guess the number I'm thinking of!")
secret_number = 7
user_guess = int(input("Guess a number from 1 to 10: "))

while user_guess != secret_number:
    print("No! Try again.")
    user_guess = int(input("Guess a number from 1 to 10: "))
    
print("You guessed it!")

