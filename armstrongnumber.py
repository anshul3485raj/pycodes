# To check whether the number is an armstrong number or not

# let the sum = 0
sum = 0

list_2 = []


for i in range(100, 1000):
    list_2.append(i)


    temp = i
    while temp > 0:
        rem = temp % 10
        sum += rem ** 3
        temp //= 10

    if i == sum:
        print(i, "is an armstrong number :)")
    else:
        print(i, "is not a armstrong number xD")
        
print(max(list_2))
