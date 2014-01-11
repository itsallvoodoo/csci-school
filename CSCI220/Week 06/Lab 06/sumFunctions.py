# sumFunctions.py
# This program will call functions that will returns sums of certain numbers
# <Chad Hobbs>

def sumN(n): # A function that returns the sum of the first n natural numbers
    natural = 0
    for r in range(1,n+1):
        natural = natural + r
    return natural

def sumNCubes(n): # A function that returns the sum of the cubes of the first n natural numbers
    cubes = 0
    for r in range(1,n+1):
        cubes = cubes + r ** 3
    return cubes

def main(): # Main program
    numbers = eval(input("Please enter how many natural numbers you want: "))
    nat = sumN(numbers)
    cub = sumNCubes(numbers)
    print("The sum of",numbers,"natural numbers is {0:.0f} and the sum of the cubes is {1:.0f}".format(nat,cub))

main()


    
