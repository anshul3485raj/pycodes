# Counting the frequencies in a list using dictionary in python

list_1 = []

frequency = {}

n = int(input("How many num u wanna add ?"))

for i in range(n):
    a = int(input("Enter the number :)"))
    list_1.append(a)


for item in list_1:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

for key, values in frequency.items():
    print("%s -> %d" % (key, values))
