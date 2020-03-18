# python program to delete any file

# importing os module
import os

# user's options
print("1. Do you want to delete file ?")
print()

print("2. Do you want to delete folder/directory ?")
print()

# choice 
choice = int(input("Enter the choice (1/2) : "))
print()

# main part
if choice == 1:
    filename = input("Enter the filename : ")
    print()
    if os.path.exists(filename):  # ".txt"
        os.remove(filename) # ".txt"
    else:
        print(filename, "not exists")
        print()

elif choice == 2:
    foldername = input("Enter the folder/directory name : ")
    print()
    if os.path.exists(foldername):
        os.removedirs(foldername)
    else:
        print(foldername, "doesn't exists")
        print()
