# To check whether the string is palindrome or not


s = input("Enter the string :)")

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # checking if both strings are equal or not
    if s == rev:
        return True
    return False


ans = isPalindrome(s)

if ans == 1:
    print("Yes")
else:
    print("No")
