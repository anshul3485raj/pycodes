# To calculate the area of triangles


# Types of triangle
# 1.Equilateral triangle
# 2.Isoceles triangle
# 3.Scalene triangle

print("1.Equilateral triangle")
print("2.Triangle")

# asking the user to input the choice
choice = int(input("Enter the choice :)"))

# for equilateral triangle
if choice == 1:
    a = int(input("Enter the value :"))
    c = (3 ** 0.5) / 4 * a ** 2
    print("Here is the area :)", c)

# for any triangle
if choice == 2:
    b = int(input("Enter the value of base :)"))
    h = int(input("Enter the value of height:)"))
    z = 1/2 * b * h
    print("Here is the area of triangle :)", z)

print(":)")