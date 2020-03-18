# python program to check whether the 
# given number is a power of 2

def pow_of_2(n):
    while (n % 2 == 0):
        n /= 2
    return n == 1

print(pow_of_2(8))
