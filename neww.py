# To prints the sum of the even indexed elements of List, minus the sum of the odd-indexed elements of List

List = [10, 39, 15, 55, 8, 77, 25, 52, 86]

even = 0
odd = 0

for i in range(len(List)):
    if i % 2 == 0:
        even += List[i]
    else:
        odd += List[i]
    z = even - odd


for j in range(len(List)):
    print("Index of",  List[j], "is :", j)


print("Even + Odd = ", z ) 

