# Heron's formula

# importing math module
import math

# asking the user to input any number
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))

# to find the value of s
s = (a + b + c) / 2

# main step of the function
z = math.sqrt(s * (s - a) * (s - b) * (s - c))

# printing results
print("approx ~", int(z))