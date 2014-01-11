# dotAlign.py
# An program that aligns a set of numbers by it's period.
# <Chad Hobbs>

t = eval(input("How many numbers would you like to align?: "))
n = []

for i in range(t):
    numbers = input("Please enter number "+str(i+1)+": ")
    n.append(numbers)
    
for i in range(t):
    piece = n[i]
    parts = piece.split(".")
    print("{0:>4.4}.{1:<3.3}".format(parts[0],parts[1][0:3]))
