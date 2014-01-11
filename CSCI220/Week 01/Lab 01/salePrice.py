## salePrice.py
## This program calculates the sale price of an item.
## <Chad Hobbs>

def main():
    itemName = input("What is the name of the item? ")
    itemPrice = eval(input("What is the list price? $"))
    itemDiscount = eval(input("What is the discount rate percent?(IE: 15% is entered as 15) "))
    itemDiscount = itemDiscount / 100
    newPrice = itemPrice - itemPrice * itemDiscount
    print("The sale price of", itemName, "is $", newPrice)

    
main()
