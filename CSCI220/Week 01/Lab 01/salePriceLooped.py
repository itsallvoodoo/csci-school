## salePriceLooped.py
## This program calculates the sale price of an item.
## <Chad Hobbs>

def main():
    n = 0
    
    
    while (n < 5):
        itemName = input("What is the name of the item? ")
        itemPrice = eval(input("What is the list price? $"))
        itemDiscount = eval(input("What is the discount rate percent?(IE: 15% is entered as 15) "))
        itemDiscount = itemDiscount / 100
        newPrice = itemPrice - itemPrice * itemDiscount
        print("The original price of ", itemName, " was $", "{0:0.2f}".format(itemPrice), " the sale price is $", "{0:0.2f}".format(newPrice), ".\n",sep="")
        n = n + 1

    print("Thank you for using my sale price calculator!")  
main()
