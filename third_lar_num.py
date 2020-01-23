# To find the third largest number from the list

# an empty list "a"
a = []

# how many elements user want to append
n = int(input("Enter the number of elements :)"))

# iterating the loop to n + 1
for i in range(1, n + 1):
    # asking the user to input a number
    b = int(input("Enter the number :)"))
    # adding each number to end of the list
    a.append(b)

# results
print("Third largest element is :)", a[n-3])