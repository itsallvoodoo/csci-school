# prog6_4.py
# This program returns a letter grade for a score using functions
# <Chad Hobbs>


def grade(score): #function that takes a score and returns a letter grade
    gradechart = ["A","B","C","D","F"]
    if score >= 90:
        i = 0
    else:
        if score >= 80:
            i = 1
        else:
            if score >= 70:
                i = 2
            else:
                if score >= 60:
                    i = 3
                else:
                    i = 4
    final = gradechart[i]
    return final


def main(): # Main program
    number = eval(input("Please enter your exam grade: "))
    
    letter = grade(number)
    
    print("Your letter grade is an",letter)



main()
