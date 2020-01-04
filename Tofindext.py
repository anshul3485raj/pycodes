# To find the extension of the file

# asking the user to enter the filename along with it's extension
filename = input("Enter the filename :")

# spliting the characters before and after .
file_extns = filename.split(".")

# printing the extension on_screen
print("Here is the extension of the file :", file_extns[-1])
