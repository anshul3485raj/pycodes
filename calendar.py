# python program to display a calendar

# importing calendar module
import calendar

# ask for month and year
yy = int(input("Enter the year : "))
print()
mm = int(input("Enter the month : "))
print()

# display the calendar
print(calendar.month(yy,mm))


