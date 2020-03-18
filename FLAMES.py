# python program to check for FLAMES

# user's name
name_1 = input("Enter the first name :" )
print()
name_2 = input("Enter the second name :" )
print()

# replacing the empty place
name_1 = name_1.replace(" ", "")
name_2 = name_2.replace(" ", "")

# condition check 
# removal of common characters
for i in name_1:
    for j in name_2:
        if i == j:
            name_1.replace(i, "", 1)
            name_2.replace(j, "", 1)
            break

# count
count = len(name_1+name_2)
print(count)

if count > 0:
    list1 = ["Friends", "Lovers", "Affectionate", "Mairrage", "Enemies"]
    while len(list1) > 1:
        c = count % len(list1)
        s_index = c - 1
        if s_index>=0:
            left = list1[:s_index]
            right = list1[s_index+1:]
            list1 = right + left
        else:
            list1 = list1[len(list1)-1]
    print("relationship is :", list1[0])

else:
    print("Enter different names !")


