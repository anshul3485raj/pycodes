# To create HaNgMaN GaMe

# importing the time module
import time

# welcoming the user 
name = input("What's your name ?")

print()

print("Hello", name, "Time to play hangman dude !!!",end="\n\n")
time.sleep(1)

print("Start guessing...",end="\n\n")
time.sleep(0.5)

# here is the secret word
word = "secret"

# create an variable with an empty value
guesses = ''

# determine the number of turns
turns = 6

# create a while loop

# check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero 
    failed = 0

    # for every char in secret_word
    for char in word:

        # see if the char is in the user guess
        if char in guesses:

            # print then out the char
            print(char)

        else:
            
            # if not found, print a dash
            print("_")

            # and increase the failed counter with one
            failed += 1

        # if failed is equal to zero

        # print you won
        if failed == 0:
            print("You won!!")
            
            # breaking the script
            break

    # ask the user to guess the word
    guess = input("Guess a character !!!")

    # set the player guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with  1 (now 9)
        turns -= 1

        # print wrong
        print("Wrong")

        # how many turns left 
        print("You have",  turns, 'more guesses')

        # if the turn is equal to zero
        if turns == 0:
            print("You loose xD")
            
            # final break for the game
            break


