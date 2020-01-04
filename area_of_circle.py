# To find the area of a circle

# importing the math module
from math import pi

# asknig the user to input the value
a = int(input("Enter the radius of circle (m/cm) :"))

# asking for the unit
unit = input("Enter the unit (m/cm) :")

# main function of the program
c = pi * (a) ** 2

# printing the results on_screen
print("Here is your area :", c, unit)
