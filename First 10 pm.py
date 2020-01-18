# To print first 10 prime numbers

while True:
 
   n = int(input("Enter how many pn :)"))

	for i in range(2 , n):
		if n % i != 0:
			print(n, end = ' ')

