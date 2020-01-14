# To check whether the number is an armstrong number or not

# let the sum = 0
sum = 0

# asking the user to input a number
n = int(input("Enter the number :"))

temp = n
while temp > 0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10

if n == sum:
    print(n, "is an armstrong number :)")
else:
    print(n, "is not a armstrong number xD")
    
