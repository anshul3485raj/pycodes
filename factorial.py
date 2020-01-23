# To find the factorial of any number

N = int(input("Enter the number :)"))

fact = 1


if N >= 1:
    for i in range(1, N+1):
        fact *= i
    print("Here is your factorial result", fact)

elif N == 0:
    print("Here is your result :)", 1)

else:
    print("Sorry factorial doesn't exist for negative numbers")