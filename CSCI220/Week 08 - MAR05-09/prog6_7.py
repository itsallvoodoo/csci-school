# prog6_7.py
# This program calculates total wages in a week given hours works and pay rate
# <Chad Hobbs>



def main(): # Main program
    hrs = eval(input("How many hours have been worked this week?: "))
    rate = eval(input("What is the pay rate for this employee?: "))

    if hrs > 40:
        wages = 40 * rate + (hrs - 40) * rate * 1.5
    else:
        wages = hrs * rate

    print()
    print("The wages for this week is ${0:0.2f}.".format(wages))


main()
