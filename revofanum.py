# python program to reverse a number

# Some basic knowledge
# 1. % >> Returns the remainder
# 2. / >> Returns the quotient(float)
# 3. // >> Returns the quotient(int)


# asking the user to input a number
n = int(input("Enter the number :)"))

# set rev = 0
rev = 0

# using a infinite loop
while(n > 0):
	# returns the remainder 
	a = n % 10
	# multipling reverse + adding remainder 
	rev = rev * 10 + a
	# returning the quotient 
	n = n // 10

# displaying results onscreen			
print(rev)

if n == rev:
	print(rev,"is a palindrome of", n)
