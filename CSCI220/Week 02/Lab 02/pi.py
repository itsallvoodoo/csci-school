# pi.py
# 
# This program approximates the value of pi using the Wallis formula
# 
# <Chad Hobbs>

print("This program approximates pi, based on how many terms you would like to use.")

n = eval(input("How many terms would you like to use?: "))
pi = 1

for i in range(2,n,2):
    pi = pi * ((i ** 2)/((i-1)*(i+1)))

pi = pi*2

print("The approximate value of pi is",pi)
