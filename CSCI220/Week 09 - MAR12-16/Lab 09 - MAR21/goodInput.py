# goodInput.py
# Forces a user to enter a number between 1 and 10
# <Chad Hobbs>

number = eval(input("Please enter a number between 1 and 10: "))

while number < 1 or number > 10:
    
    print("You entered",number,"which is not between 1 and 10.")
    number = eval(input("Enter a number between 1 and 10: "))

print("Your number is",number)
