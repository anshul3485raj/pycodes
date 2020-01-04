# creating all possible number out a gievn number

# importing random module
import random

# importing math module
import math
# asking the user to how many times to run the loop
n = int(input("How many numbers u want to shuffle ?"))

int_list = [ ]


for i in range(n):
	# asking the user to input a number
	n = int(input("Enter the number :)"))
	int_list.append(n)


for j in range(math.factorial(len(int_list))):
	# shuffling all integers with each other
	random.randrange(int_list)
	# joining and printing all possible outcomes
	print(int_list)
