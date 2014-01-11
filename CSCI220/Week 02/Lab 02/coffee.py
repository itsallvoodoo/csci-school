# coffee.py
#
# A program that computes the cost of coffee orders for customers
#
# <Chad Hobbs>

orders = eval(input("How many orders do you want to process?: "))

for i in range(1, orders+1):
    print("For order number", i)
    pounds = eval(input("Pounds of coffee: "))
    total = (pounds * 10.5) + (pounds * .86) + 1.50
    print("Cost for order ",i , " is: $", "{0:0.2f}".format(total), sep="")
    print()
    
    
