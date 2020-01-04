# guessing a secret number in python


# importing modules
import random

# secret_num user has to guess
secret_num = random.randint(1, 100)

# the number guessed by user
guess = int(input("Enter the number :)"))

# number of turn
turn = 6

while True:
	if guess == secret_num:
		print("You won :)")

	elif guess < secret_num:
		turn -= 1
		print("Too low :(")

	elif guess > secret_num:
		turn -=1
		print("Too high :(")

	elif turn == 0:
		n = input("Do you want to play again xD ?")
		if n == "y" or "Y":
            print("Let's begin ..")
	else:
		print("Thanks for playing :O")
		break
