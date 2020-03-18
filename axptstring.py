# Python program to accept the
# string which contains all the vowels

# user input
string = input("Enter the string : ")

for i in string:
    if i == "a" and i == "e" and i == "i" and i == "o" and i == "u":
        print("The string", string, "is accepted because it conatins all vowels")
        break
    else:
        print("Not accepted because it lacks some vowels")
        break
