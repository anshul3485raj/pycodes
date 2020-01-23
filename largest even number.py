# To find the largest even number from the list

# creating an empty list
Even = []

# asking the user to append how many numbers
length = int(input("How many numbers you want to add :)")) 

# running a for loop
# asking the user to enter the num
for i in range(length):
    a = int(input("Enter the number :)"))
    Even.append(a)

# printing the list
print("Even =", Even)

# printing another for loop 
# To find the max even num from list
for j in Even:
    if j % 2 == 0:
        z =  max(Even)
        print("Here is the largest even number :)", z)
        break
    else:
        print("No even number is present xD")
        break
