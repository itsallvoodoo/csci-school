# gradeToLetter.py
# This program will convert numerical grades into letter grades
# <Chad Hobbs>

gradechart = ["A","B","C","D","F"]

grade = eval(input("Please enter your exam grade: "))

if grade >= 90:
    i = 0
else:
    if grade >= 80:
        i = 1
    else:
        if grade >= 70:
            i = 2
        else:
            if grade >= 60:
                i = 3
            else:
                i = 4

print("Your letter grade is",gradechart[i])

