# python program to tell the horoscope 

#importing random module
import random 

# importing time module
import time

# name
name = input("What's your name ? ")
time.sleep(0.5)

# age
age = input("What's your age ? ")
time.sleep(0.5)

# D.O.B
DOB = input("What's your date of birth ? ")
time.sleep(0.5)
print()

# Profession
Profession = ["Software Engineer", "Teacher", "Scientists",
"Comedian", "Actor", "Doctor", "Prime Minister"]

# salary
salary = ["30k", "100k", "Millionaire", "Billionaire", "10k", "500k"]

c = random.choice(Profession)

d = random.choice(salary)

print("Your profession will be :", c, end="\n\n")

print("Your salary per annum will be :", d, end="\n\n")