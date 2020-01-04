# creating all possible string from vowels
# or anagram program

# importing random module
import random

# importing math module
import math

# creating a char_list
char_list = ['a', 'y', 'u', 's', 'h']


for i in range(math.factorial(len(char_list))):
    # shuffling all vowels with each other
    random.shuffle(char_list)
    # joining and printing the chars
    print( ' '.join(char_list))

