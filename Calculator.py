# Script to make a standard calculator
   

# importing math module
import math



# Various functions of the standard calculations
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Power')
print('6.Factorial')
print("7.Square_root")


# asking the user to enter his choice
choice = int(input("Enter youe choice :"))

# defining various methods

# defining the addition function
def add():
    x = 0
    n = int(input("How many numbers you want to add :"))
    for i in range(n):
        a = int(input("Enter the number :"))
        x += a
    print("Here is your total :", x)


# defining the subtraction function
# some prblm need to be fixed
def sub():
    x = 0
    n = int(input("How many numbers you want to subtract :"))
    for i in range(n):
        a = int(input("Enter the number :"))
        x += a
    print("Here is your result", x)

# defining the multiplication function
def mul():
    x = 1
    n = int(input("How many numbers you want to multiply :"))
    for i in range(n):
        a = int(input("Enter the number :"))
        x *= a
    print("Here is your total :", x)

# defining the division function
def div():
        a = int(input("Enter the number :"))
        b = int(input("Enter the number :"))
        if a > b:
            print("Here is your quotient :",  a // b)
            print("Here is your remainder :", a % b)
        else:
            print("Invalid input !!!")


# defining the power function
def pow():
    a = int(input("Enter the number :"))
    b = int(input("Enter the exponential power :"))
    c = math.pow(a, b)
    print("Here is your result :", int(c))


# defining the factorial function
def fac():
    z = int(input("Enter the number :"))
    if z > 0:
        c = math.factorial(z)
        print("Here is your factorial :", c)
    else:
        print("Invalid input !!!")


# defining the sqrt function
def sqrt():
    s = int(input("Enter the number :"))
    if s > 0:
        c = math.sqrt(s)
        print("Here is sqrt :", c)





# main loop of the program
while True:
    if choice == 1:
        add()
        break

    if choice == 2:
        sub()
        break

    if choice == 3:
        mul()
        break

    if choice == 4:
        div()
        break

    if choice == 5:
        pow()
        break

    if choice == 6:
        fac()
        break

    if choice == 7:
        sqrt()
        break