
# Score 
Score = 0

# Failed 
Fail = 0

# To create a word game

# importing time module
import time

while True:
    # welcoming the user 
    name = input("Enter your name :")
    print()

    print("Hello", name, "time to guess some words...")
    time.sleep(0.5)
    print()

    print("Start guessing ...", end="\n\n")
    time.sleep(0.5)

    # Main game
    print("1.", "C _ _ _ _ A ?" )
    print()

    print("[HINT]", ":-", "Movies, Theatres")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_1  = input("Enter the word :").lower()
    print()

    if ans_1 == "cinema":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    print("2.", "T _ _ I _ _ S _ _ _ ?")
    print()

    print("[HINT] :- Electronic device on which we can see and hear anything !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_2 = input("Enter the word :").lower()
    print() 

    if ans_2 == "telivision":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    print("3. C _ L _ _ _ E _ ?")
    print()

    print("[HINT] :- The amount of potential someone contains to do something !!!")
    print()


    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_3 = input("Enter the answer :").lower()
    print()

    if ans_3 == "calliber":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1 
    print()

    print("4. _ A _ _  O _  ?")
    print()

    print("[HINT] :- A beautiful band of seven colours seen in sky !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_4 = input("Enter the word :").lower()
    print()

    if ans_4 == "rainbow":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    print("5. T _ S _ ?")
    print()

    print("[HINT] :- Examination !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_5 = input("Enter the word :").lower()
    print()

    if ans_5 == "test":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1

    print()

    print("6. _ O _ O _ H _ _ E _ ?")
    print()

    print("[HINT] :- The words which sounds same but have different meanings !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_6 = input("Enter the word :").lower()
    print()

    if ans_6 == "homophones":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrecct xD")
        Fail += 1
    print()

    print("7. P _ _ I _ _ _ O _ E ?")
    print()

    print("[HINT] :- The words which are same from forward and backward !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_7 = input("Enter the word :").lower()
    print()

    if ans_7 == "palindrome":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    print("8. _ N _ _ A _ _ A _ ?")
    print()

    print("[HINT] :- The most popular social media app !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_8 = input("Enter the word :").lower()
    print()

    if ans_8 == "instagram":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    print("9. C _ _ P _ _ _ R ?")
    print()

    print("[HINT] :- The device commanly used for trade and educational purposes !!!")
    print()

    print("Guess the complete word !!!")
    time.sleep(0.5)
    print()

    ans_9 = input("Enter the word :").lower()
    print()

    if ans_9 == "computer":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    print("10. _ B _ C _ _ ?")
    print()

    print("[HINT] :- The first device invented for basic calculations !!!")
    print()

    print("Guess the complete word !!!")
    print()

    ans_10 = input("Enter the answer :").lower()
    print()

    if ans_10 == "abacus":
        print("Correct :)")
        Score += 1
    else:
        print("Incorrect xD")
        Fail += 1
    print()

    if Score == 10:
        print("You won", name, "!!!")
        continue
        print()
    
    elif Fail == 6:
        print("Sorry you lose", name, "!!!")
        break
    
    else:
        choose = input("Do you want to play again ? (Y/N)").lower()
        if choose == "y":
            continue
        
        elif choose == "n":
            print("Byee...")
            break 


            

        