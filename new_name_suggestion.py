# python program to suggest random names 

# importing random module
import random

# Date_of_Birth
DOB = input("Enter the Date_of_Birth : ")
print()

# Gender 
print("1. Male(M)", end="\n\n")

print("2. Female(F)",end = "\n\n")

# user's gender selection
choice = input("Enter the gender : ").lower()
print()

# random names
names = ["William", "Michael", "James", "Clay",
"Adam", "John", "Jimmie", "Jamey", "Rob", "Justin", 
"Steve", "Mark", "Tim", "Timmie", "Tom", "Peter", "David"]

name_2 = ["Jennifer", "Katherine", "Hannah", "Cloie",
"Anne", "Marie", "Julia", "Ellen", "Stephanie"]

if choice == "m" or choice == "male" or choice == "1":
    rand_name = random.choice(names)
    print("Here is your random name :", rand_name)
    print()

elif choice == "f" or choice == "female" or choice == "2":
    rand_name_2 = random.choice(name_2)
    print("Here is your random name :", rand_name_2)
    print()

else:
    print("Invalid input !!!")