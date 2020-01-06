# To create random of password of any length

# importing string module
from string import ascii_letters as asc, digits as d

n = int(input("Enter the length :)"))

for i in range(n):
    a = asc  + d
    print("Here is your password"," ".join(a))
    break