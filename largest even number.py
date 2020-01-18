# To find the largest even number from the list

Even = []

length = int(input("How many numbers you want to add :)")) 

for i in range(length):
    a = int(input("Enter the number :)"))
    Even.append(a)

print("Even =", Even)

for j in Even:
    if a % 2 == 0:
        z =  max(Even)
        print("Here is the largest even number :", z)
        break
    else:
        print("No even number is present xD")
        break
