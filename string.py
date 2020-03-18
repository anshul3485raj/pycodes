""" >To calculate length of string
> To check vowel and consonants
> no. of consonants and vowel"""

# user input
word = input("Enter the word :")
print()

# vowels
vow = []

# consonants
con = []

# count_vow
count_vow = 0

# count_con
count_con = 0

# looping through word
for i in word:
	if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
		vow.append(i)
		count_vow += 1

print("Vowels = ", vow)
print()
print("No. of vowels are :", count_vow)
print()

	else:
		con.append(i)
		count_con += 1
print("Consonants = ", con)
		print()
		
print("No. of consonants are :", count_con)
		print()

# to calculate length of string
print("The length of string is :", len(word))