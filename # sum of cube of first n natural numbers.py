 #sum of cube of first n natural numbers

n = int(input("Enter the series length :"))

def Sum_of_Series(n):
	sum = 0
	for i in range(0, n + 1):
		sum += i*i*i
		return sum

	print(Sum_of_Series(n))