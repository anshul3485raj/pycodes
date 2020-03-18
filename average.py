# To find the average sum of marks of 5 sujects and grades

# number of subjects
n = 5

# marks of subjects
Sub_1 = int(input("Enter the marks of English :)"))
Sub_2 = int(input("Enter the marks of Hindi:)"))
Sub_3 = int(input("Enter the marks of Mathematics:)"))
Sub_4 = int(input("Enter the marks of Science:)"))
Sub_5 = int(input("Enter the marks of S.S.T:)"))

# finding the average sum of total marks
average = (Sub_1 + Sub_2 + Sub_3 + Sub_4 + Sub_5) / n

print("Average Marks :)", average)

if average >= 90:
    print("Your grade is :", "A+")
elif average < 90 and average > 80:
    print("Your grade is :", "A")
else:
    print("Your grade is :", )
