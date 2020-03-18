# To create a quiz that ask random questions from the user


# Things required to develop the quiz game
# users input or anwer
# types of questions
# no . of questions
# category for questions
# if user answer is correct rewarding them one point and nothing if ans is wrong


# categories for types of questions
print("1.Mathematics")
print()
print("2.General Knowledge")
print()
print("3.Technology")
print()
print("4.Current affairs")
print()
print("5.Entertainment")
print()

# importing modules


# importing time module
import time

# importing random modules
import random


# Welcoming the user 
name = input("What's your name ?")
print()


print("Hello", name, "let's begin this quiz ...")
time.sleep(0.5)
print()

# asking the user to enter choice for selecting any one category
choice = int(input("Please select the category :"))
print()

# points 
points = 5


# failed or incorrect answer
failed = 0



if choice == 1:
    print("Let's begin the mathematics quiz..")
    time.sleep(0.5)



    print(name, "you have to answer five questions!!")
    print()

    print("Here is your first question..",end="\n\n")
    time.sleep(0.5)


    print("1. What is the factorial of zero ?")
    ans_1 = input("Enter the answer :").lower()
    if ans_1 == "one" or ans_1 == "1":
        print("Correct !!!")
    else:
        print("Incorrect !!!")



    print("Here is your next question...",end="\n\n")
    time.sleep(0.5)

    print("2. Does factorial exists for negative numbers ?")
    ans_2 = input("Enter the answer :").lower()
    if ans_2 == "no" or ans_2 == "No" or ans_2 == "NO" or ans_2 == "nO":
        print("Correct !!!")
    else:
        print("Incorrect !!!")

    print()
    print("3. Which is the smallest composite number ?")
    ans_3 = int(input("Enter the answer :"))
    if ans_3 == 4:
        print("Correct !!!")
    else:
        print("Incorrect !!!")

    print()

    print("4. Which is the smallest prime number ?")
    ans_4 = int(input("Enter the answer :"))
    if ans_4 ==2:
        print("Correct !!!")
    else:
        print("Incorrect !!!")

    print()

    print("5. What is the value of pi ?")
    ans_5 = input("Enter the answer :")
    if ans_5 =="3.14" or ans_5 =="22/7":
        print("Correct !!!")
    else:
        print("Incorrect !!!")  





# General knowledge
if choice == 2:
    print("Let's begin the general knowledge quiz..")
    time.sleep(0.5)

    print(name, "you have to answer five questions!!")
    print()

    print("Here is your first question..",end="\n\n")
    time.sleep(0.5)

    print("1. How many continents are in the world ?")
    ans = int(input("Enter the answer :"))

    if ans == 7:
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1
    print()

    print("Here is the next question ...")
    time.sleep(0.5)

    print()

    print("2. Which is the largest country in the world ?")
    ans = input("Enter the answer :").lower()

    if ans == "russia":
        print("Correct !!!")
    else:
        print("Incorrect ")
        failed += 1
        points -= 1

    print()

    print("3. Who is the current prime Minister of India ?")
    print("Only mention first and last name..")
    ans = input("Enter the answer :").lower()

    if ans == "narendra modi" or ans == "narendramodi":
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1
    print()


    print("4. Who is honoured by the title", "MISSILE MAN OF INDIA")
    ans = input("Enter the answer :")
    if ans == "apjabdulkalam" or ans == "apj abdul kalam":
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1
    print()


    print("5. In year 2020 India celebrated it's which Republic Day ?(number)")
    ans = int(input("Enter the number :"))
    if ans == 71:
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1
    print()


if choice == 5:
    print("Let's begin the Entertainment round")
    time.sleep(0.5)
    print()

    print(name, "you have to answer five questios !")
    time.sleep(0.5)
    print()

    print("Here is your first question !")
    time.sleep(0.5)
    print()

    print("1. Who is the lead actor in the movie Dabaang 3 ?")
    ans = input("Enter the answer :").lower()

    if ans =="salmankhan" or ans == "salman khan":
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1

    print("Here is your next question")
    time.sleep(0.5)
    print()

    print("2. Who is popularly known for his famous dialouge", "Abey Saale !")
    ans = input("Enter the answer :")
    
    if ans == "harmonium chacha" or ans == "harmoniumchacha":
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1

    print("3. What is the expanded form of PUBG ?")
    ans = input("Enter the number :")
    if ans == 'player unknowns battle ground' or "playerunknownbattleground":
        print("Correct !!!")
    else:
        print("Incorrect !!!")
        failed += 1
        points -= 1



# Technology

if choice == 3:
    print("Let's begin the general knowledge quiz..")
    time.sleep(0.5)

    print(name, "you have to answer five questions!!")
    print()

    print("Here is your first question..",end="\n\n")
    time.sleep(0.5)

    print("1. Who was the founder of Apple Company ?")
    ans_1 = input("Enter the answer :").lower()
    if ans_1 == "steve jobs" or ans_1 == "stevejobs":
        print("Correct !!!")
    else:
        print("Incorrect !!!")



































# Do you want to player further of quit
while True:
    if points == 0 and failed == 3:
        print("You Loose !!!")
        break

    elif points == 5 and failed == 0:
        print("Congratulations you won !!!")
        break

    
