# password generator for python

# importing modules
import string

import random

# defining pw_gen function
# for generation of random passwords
def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return " ".join(random.choice(chars) for _ in range(size))


# printing the random password onscreen
print(pw_gen(int(input("How many characters in your password ?"))))



