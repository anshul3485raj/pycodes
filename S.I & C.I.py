# To find simple interest and compound interest

# Two types of interest
print("1.Simple Interest")
print("2.Compound Interest")

# asking for the user's choice
choice = int(input("What's your choice ?"))


if choice == 1:
    P = int(input("Enter the Principal :)"))
    R = int(input("Enter the Rate :)"))
    T = int(input("Enter the Time :)"))
    Simple_Interest = P * R * T / 100
    print("Simple Interest", Simple_Interest)

if choice == 2:
    pass