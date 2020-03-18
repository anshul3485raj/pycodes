# python program to tell the position of character

# count
count = 0

# words
words = input("Enter the word : ")

# char
char = input("Which char position u want ?")

if char in words:
    c = words.find(char)
    print("char position is :", c)

else:
    print(char, "is not present !")

 