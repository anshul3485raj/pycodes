# To show the current date & time

# importing the datetime module
import datetime

# using the now function to tell the current date and time
now = datetime.datetime.now()

# printing the current date and time
print("Current_date_and_time_is :")

# converting the date and time in string format
print(now.strftime("%Y-%m-%d %H:%M:%S"))