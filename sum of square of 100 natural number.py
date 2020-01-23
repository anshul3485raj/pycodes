# To find the sum of the square of the first 100 natural numbers

# value of sum is 0
sum = 0

# iterating the loop to 100
for i in range(1, 101):
    # squaring each number
    c = i ** 2
    # adding the each squared number
    sum += c

# results
print("Here is the total sum :)", sum)

