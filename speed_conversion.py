# conversion of km/hr into m/sec or vice versa

# importing time module
import time


# choice for speed conversion
print("1.km/hr into m/sec")
print("2.m/sec into km/hr")


choice = int(input("Enter the choice :"))


# asking the user to input speed 
n = int(input("Enter the magnitude of speed :"))


if choice == 1:
	c = n * (5 / 18)
	print("Here is your result :", c, "m/sec" )
	time.sleep(0.5)


elif choice == 2:
	a = n * (18 / 5)
	print("Here is your result :", a, "km/hr")
	time.sleep(0.5)

else:
	print("Invalid choice input !!!")
	time.sleep(0.5)
