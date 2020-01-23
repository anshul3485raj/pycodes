# To find the largest and smallest number from the list 

# an empty list
list_1 = []

# how many numbers user wants to add to list
n = int(input("How many numbers u wanna add :)"))

# iterating the loop to n + 1
for i in range(1, n+1):
    # asking the user to input a num
    b = int(input("Enter the number :)"))
    # adding each num to end of list
    list_1.append(b)

# the list
print("List =", list_1, end="\n\n")

# largest num
print("Largest number is :", max(list_1), end="\n\n")

# smallest num
print("Smallest number is :", min(list_1), end="\n\n")



