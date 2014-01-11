# newton.py
#
# This program approximates the square root of a number
#
# < Chad Hobbs >

print("Let's calculate square roots!")
print()

square = eval(input("What number would you like to take the square root of?: "))
approx = eval(input("How many times would you like to improve the approximation?: "))
root = square / 2

for i in range(1,approx):
    root = ((root + (square / root))/2)

print()
print("The approximate square root of ",square," is ",root,".",sep="")
