# working with arrays

# importing array module
from array import *

# an empth array
arr = array('i', [])

# asking the user for a range
n = int(input("Enter the range :"))

# using a for loop
for i in range(n):

    # asking the user to input a number
   a = int(input("Enter the number :)"))

   # adding each value to the last of array
   arr.append(a)

# printing the results
print(arr)
