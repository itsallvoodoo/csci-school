# prog3_4.py
# A program that prompts for deposits and withdrawals and then prints the balance 
# <Chad Hobbs>

n = eval(input("Please enter the number of transactions you would like to make: ")) # gets transactions
bal = eval(input("Please enter your initial balance: $")) # gets initial balance

# creates all of the lists
trans_num = []
trans_amount = []
balance = []

for i in range(1,n+1): # runs through all of the transactions
    change = eval(input("Enter the amount for transaction "+str(i)+": $"))
    bal = bal + change
    # adds all of the data to the various lists
    trans_num.append(i)
    trans_amount.append(change)
    balance.append(bal)
    print("Your new balance is ${0:0.2f}".format(balance[i-1]))

print()
print()
print("     #     Transaction     Balance")
print("-"*40)

for i in range(len(trans_num)): # prints the stored data in a formatted list
    print("{0:^12}${1:<15.2f}${2:<8.2f}".format(trans_num[i],trans_amount[i],balance[i]))
                  
