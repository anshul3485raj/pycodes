# To create a fibonacci sequene in python

# asking the user to input how 
# long fibonacci series wanted 
num = int(input("Enter the number :)"))

# For example a series like :-
# 0, 1, 1, 2, 3, 5, 8, 13, .....

# defining a fib function
def fib(n):

    # let the value of a = 0
    a = 0
    # let the value of b = 1 
    b = 1

    # if user enters 1 he/she
    # will recieve a 0
    if n == 1:
        print(a)
    
    # user will get a fibonacci sequence
    else:
        print(a)
        print(b)

        # to iterate the string from 2 to n - 1
        for x in range(2, n):
            
            # c = a + b i.e., 0 + 1
            c = a + b
            # swapping to the next number
            a = b
            b = c
            # printing the fib series
            print(c)

fib(num)
    