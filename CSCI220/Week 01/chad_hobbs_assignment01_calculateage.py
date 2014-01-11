# assignment01-calculateage.py -------- Age calculation program with errorchecking
# Written 18JAN12

#module calls
import time;

#initialize true/false variables
birth_check = 0

name = input("What is your name? ")

#birth year validation loop
while birth_check == 0:
    year_born = eval(input("What year were you born (19xx)? "))
    if year_born < 2000 and year_born > 1899:
        birth_check = 1
    else:
        print("That year is too high or too low.")

#current year error check
current_year = eval(input("Enter the current year: "))
localtime = time.localtime(time.time())
if current_year != localtime.tm_year:
    print ("I don't believe you, but we'll go with that number.")

#evaluated outputs
age = current_year - year_born
print(name, "was born in", year_born, "and is either", age - 1, "or", age, "years old.")
