# Rock Paper Scissors game

# Concepts :-
#1 Rocks beats Scissors
#2 Scissors beats Paper 
#3 Paper beats Rocks

# importing modules
import sys
import time
import random


# Main loop of the game
# asking the user for name
user1 = input("What's your name ?")
time.sleep(0.5)

print("\nHeyy", user1, "Lets begin...")
time.sleep(0.5)

player = False

# asking the user to select his/her choice
player = input("What's your choice Rock, Paper, Scissors ?")


t = ["Rock", "Paper", "Scissors"]

computer = random.choice(t)

while True:
    player = input("Rock", "Paper", "Scissors")
    if player == computer:
        print("It's a tie !!!")

    elif player == "Rock" or "r":
        if computer == "Paper":
            print("Paper win !!!")
        else:
            print("Scissors win !!!")

    elif player == "Paper" or "p":
        if computer == "Scissors":
            print("Scissors win !!!")
        else:
            print("Rock win !!!")


    elif player == "Scissors" or "s":
        if computer == "Rock":
            print("Rock win !!!")
        else:
            print("Paper win !!!")


    else:
        print("It's a invalid input plzz try again !!")
        
    print("Do you want to play again (Y/N) :")
    ans = input()

    if ans == "Y" or "y":
        player == True
    else:
        player == False
        sys.exit 



