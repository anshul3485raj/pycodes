# To check whether the number is prime or not

# asking the user to input a number
num = int(input("Enter the number :)"))


# If the number is greater than 1
if num > 1:


	# Iterate from 2 to n //2
	for i in range(2, num//2):

		# If num is divisible by any number b/w
		# 2 and n //2, it is not a prime 	
		if num % i == 0:
			print(num, "is not a prime number")
			break

	# else the number is prime
	else:
		print(num, "is a prime number")

	# otherwise the number is not a prime
else:
	print(num, "is not a prime number")