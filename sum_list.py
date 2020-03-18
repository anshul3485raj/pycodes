# python script to get sum of all listed elemets

# empty list
list_1 = []

# sum
sum = 0

# how many times
n = int(input("Enter how many times :"))
print()

# append to loop
for i in range(n):
    a = int(input("Enter the number :"))
    list_1.append(a)
print()

# print the list
print("List_1 : ", list_1, end="\n\n")

# adding each value
for x in list_1:
    sum += x

print("The sum is : ", sum)


