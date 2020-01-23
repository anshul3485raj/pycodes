# To find the largest number among three numbers

# To ask the user for the input
A = int(input("Enter the number :)"))
B = int(input("Enter the number :)"))
C = int(input("Enter the number :)"))

# conditions for finding the largest number
if A > B and A > C:
    print(A, "is the lagest number")
elif B > A and B > C:
    print(B, "is the largest number")
elif C > A and C > B:
    print(C, "is the largest number")
else:
    print("All are same xD")

    