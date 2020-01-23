# To find out the sum of the digits of the entered numbers

# ask the user to enter the integer as a str
num = input("Enter the number :)")

# initial value of sum = 0
sum = 0

# iteratinf loop through a str
for z in num:
    # converting string into int and adding value
    sum += int(z)

# results
print("Here is your result", sum)
