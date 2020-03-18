# python program to read and write to files

f = open("ayush.txt", "x")
f.write("My name is Ayush Negi")
f.close()

f = open("ayush.txt", "r")
print(f.read())
