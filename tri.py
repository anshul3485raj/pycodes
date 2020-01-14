

# importing math module
import math

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))

# to find the value of s

s = (a + b + c) / 2


z = math.sqrt(s * (s - a) * (s - b) * (s - c))


print(z)