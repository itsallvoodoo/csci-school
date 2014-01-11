## BirthdayInfo.py
## This program gets personal info about the user and calculates their
## birthday.
## <Chad Hobbs>

def main():
    print ("I will calculate your age. Please answer the following.\n")
    thisYear = 2012
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    birthYear = eval(input("Enter the year of your birth: "))
    age = thisYear - birthYear
    print ("Hello", first, last)
    print ("You will turn", age, "years old this year.")
    
main()
