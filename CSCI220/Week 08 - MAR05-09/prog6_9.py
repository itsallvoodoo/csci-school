# prog6_9.py
# This program returns a babysitting bill based on start and stop times
# <Chad Hobbs>





def main(): # Main program
    bill = 0
    flag = 0
    while flag != 1:
        start = input("Please enter at what time the babysitter started in hh:mm format(ie: 5:15 am) ")
        finish = input("Please enter at what time the babysitter ended in hh:mm format(ie: 10:30 pm) ")

        if len(start) < 7 or len(start) > 8 or len(finish) < 7 or len(finish) > 8:
            flag = 0
            print()
            print("The formating of your input is not correct. Please try again.")
        else:
            flag = 1

    # This part formats the starting time input into usable numbers
    st = start.split(":")
    st[0] = int(st[0])
    if st[1][3] == 'p' or st[1][3] == 'P':
        st[0] = st[0] + 12
    st[1] = int(st[1][0:1])
    st_time = st[0] + st[1] / 60

    fi = finish.split(":")
    fi[0] = int(fi[0])
    if fi[1][3] == 'p' or fi[1][3] == 'P':
        fi[0] = fi[0] + 12
    fi[1] = int(fi[1][0:1])
    fi_time = fi[0] + fi[1] / 60
    
    if fi_time > 21:
        if st_time > 21:
            bill = (fi_time - st_time) * 1.75
        else:
            bill = (fi_time - 21) * 1.75 + (21 - st_time) * 2.50
    else:
        bill = (fi_time - st_time) * 2.50

    print()
    print("The babysitter bill is ${0:.2f}.".format(bill))
        



main()
