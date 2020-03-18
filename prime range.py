for n in range(100, 1001):

    if n  > 1:

        for i in range(2, n//2):
            if n % i != 0:
                print(n)

            else:
                break
