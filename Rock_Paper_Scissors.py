     # Rock Paper Scissors game

# Concepts :-
#1 Rocks beats Scissors
#2 Scissors beats Paper 
#3 Paper beats Rocks

# importing the system & time module
import sys
import time

# asking the user for name and their choices..
User_1 = input("What's your name ?")
time.sleep(1.5)

User_2 = input("And your name ?")
time.sleep(1.5)

User_1_answer = input("%s, do you want to choose rock, paper, scissors?" % User_1)
User_2_answer = input("%s, do you want to choose rock, paper, scissors?" % User_2)


# Main game loop
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie !!!")
        time.sleep(1)
    
    elif u1 == "Rock":
        if u2 == "Scissors":
            return("Rock wins !!!")
            time.sleep(1)
        else:
            return("Paper wins!!!")
            time.sleep(1)

    elif u1 == "Scissors":
        if u2 == "Paper":
            return("Scissors wins !!!")
            time.sleep(1) 
        else:
            return("Rock wins !!!")
            time.sleep(1)

    elif u1 == "Paper":
        if u2 == "Rock":
            return("Paper wins !!!")
            time.sleep(1)
        else:
            return("Scissors wins !!!")
            time.sleep(1)

    else:
        return("Invalid input !!!, Plzz try once again ...")
        time.sleep(0.5)
        sys.exit


# printing the final result
print(compare(User_1_answer, User_2_answer))
time.sleep(2.5)


 