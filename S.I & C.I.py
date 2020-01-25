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
    def compound_interest(principle, rate, time):
         result = principle * (pow((1 + rate / 100), time))
         return result
            
            p = int(input("Enter the principal amount:"))
            r = int(input("Enter the interest rate: "))
            t = int(input("Enter the time in years: "))
        
            amount = compound_interest(p, r, t)
            interest = amount - p

            print("Compound amount is :", amount)
            print("Compound amount is :", interest)