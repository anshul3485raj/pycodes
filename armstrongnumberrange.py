# To test if the number is equal to sum of cube of it's digits from 100 to 1001

# iterating the loop from 100 to 1001
for N in range(100, 1001):
    # Let M = N
    M = N
    # let initial value of Sum = 0
    Sum = 0

    # Till N isn't equal to 0
    while (N != 0):
        Rem = N % 10
        Sum = Sum + Rem ** 3
        N = N // 10

    # if M == Sum printing that number
    if (M == Sum):
        print(M)

