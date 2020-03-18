# Python program to check for harshad number 

# sum 
sum = 0

# user's input
num = int(input("Enter the number : "))

n = num

# main loop
while num > 0:
    a = num % 10
    sum += a
    num = num // 10

if n % sum == 0:
    print("It's a harshad number !")
else:
    print("It's not a harshad number !") 