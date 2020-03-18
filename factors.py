# To find the factors of any number 

# asking the user to enter the number 
num = int(input("Enter the number :"))

for i in range(1, num + 1):
	if num % i == 0:
		print(i)
		