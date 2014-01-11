# findNumber.py
# Finds the number entered in a list and prints it's position.
# <Chad Hobbs>

number = eval(input("Enter an integer: "))

numlist = [1,3,5,7,9,11,13,15,17,19]
index = 0
while index < 10:
    if numlist[index] == number:
        print("The integer enterered is in position",index+1)
        index = 11
    else:
        index = index + 1

if index == 10:
    print("Your number was not in the list.")
