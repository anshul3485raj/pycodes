# checking whether the voter is eligible for voting or not

# The eligibility criteria for voting is for 18 or above people

n = int(input("What's your age ?"))

def age(n):
    if n >= 18:
        print("You are eligible for voting")
    else:
        print("Sorry u can't vote")

age(n)
