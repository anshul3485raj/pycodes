# To append random numbers to a list

# importing random module
import random

# Create a empty string
num = []


for i in range(10):
    c = random.randint(1, 100)
    num.append(c)

print("num =", num)