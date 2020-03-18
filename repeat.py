# python program to create a func.
# that repeats a value two times

# replet function
def replet():
    s = input("Enter the word/letter/sentence : ")
    for i in s:
        c = i*2
        print(c, end="")

# calling the func.
replet()

