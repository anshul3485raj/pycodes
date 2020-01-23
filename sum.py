# To find the sum of the entered numbers

n = int(input("How many numbers u wanna add ?"))

sum = 0

for i in range(n):
    a = int(input("Enter the number :)"))
    sum += a

print("Here is your total :)", sum) 

