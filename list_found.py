# to check whether the element
# is present in list or not

# user input
user = int(input("Enter any number :"))

# list
List = [12, 15, 10, 85, 36, 55, 100, 99, 105]

# main loop 
for i in List:
    if user in List:
        print("Found")
        break
    else:
        print("Not found")
        break