# numDigits.py
# A program that asks for a postive integer and quits when given an integer less than 0
# <Chad Hobbs>

number = 1

while number > 0:

    number = eval(input("Please enter a positive integer: "))

    if number > 0:
        digits = 0
        numDigits = number
        while  numDigits != 0:
            numDigits = numDigits // 10
            digits = digits + 1

        print("")
        print("The number",number,"has",digits,"digits.")
