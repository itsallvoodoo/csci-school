# prog6_8.py
# This program returns a letter grade for a score using decisions
# <Chad Hobbs>





def main(): # Main program
    number = eval(input("Please enter your exam grade: "))

    gradechart = ["A","B","C","D","F"]

    if number >= 90:
        i = 0
    else:
        if number >= 80:
            i = 1
        else:
            if number >= 70:
                i = 2
            else:
                if number >= 60:
                    i = 3
                else:
                    i = 4
        
    print("Your letter grade is an",gradechart[i])



main()
