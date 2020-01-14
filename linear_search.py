# linear search program implementation in python

# importing the system module
import sys


# asking the user for the choice
print("1.String linear search")
print("2.Integer linear search")

z = int(input("Enter the choice :"))

if z == 1:
        # for string format        
        arr = ['ayush', 'anas', 'shubham', 'sachin', 'lakshaya']

        what = input("What do you want ?")

        for i in range(len(arr)):
                if what in arr:
                     print(what, "it is present :)")
                     break
                else:
                        print("It's not present :(")
                        break
                
elif z == 2:			
        # for integer format

        # importing random module
        import random
        chance = 6

        arr = [132, 11, 15, 22, 19, 25, 10]

        n = int(input("Enter the number :" ))

        for i in range(len(arr)):
                if n in arr:
                        print("You guessed it ri8 :)")
                        break
                else:
                        print("sry ur wrong")
                        chance -= 1
                        break
                if chance  == 0:
                        print("Sorry you lose !")
                        break

else:
        print("It's an invalid input !")
        sys.exit()
