# To print a triangle pyramid pattern of numbers

N = int(input("Enter the number :)"))


for i in range(1, N+1):
    for j in range(N + 1 - i):
        print(" ", end = ' ')
    for j in range(1, i):
        print(j, end = " ")
    for i in range(i, 0, -1):
        print(i, end=" ")

    print("\n")