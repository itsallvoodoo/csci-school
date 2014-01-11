# prog6_10.py
# This program calculates whether or not the given year is a leap year
# <Chad Hobbs>





def main(): # Main program
    y = eval(input("What is the year you would like to know about?: "))
    print()
    yr = str(y)
    if (y % 4) == 0:
        if yr[-2:] == '00' and (y % 400) != 0:
            print(y,"is not a leap year!")
        else:
            print(y,"is a leap year!")

    else:
        print(y,"is not a leap year.")



main()
