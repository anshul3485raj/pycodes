"""To read all the number from the list
if the element is a multiple of 5 multiply 
it by 2 else multiply by 3"""

List_1 = [10, 11, 15, 23, 71]

List_2 = []

for i in List_1:
	if i % 5 == 0:
		x = i * 2 
		print(x)
		List_2.append(x)

	else:
		y = i * 3
		print(y)
		List_2.append(x)

print("Here is your list :", List_2, end=", ")

