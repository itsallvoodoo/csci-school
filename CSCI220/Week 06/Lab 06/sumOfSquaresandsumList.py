# sumOfSquaresandsumList.py
# This program will call functions that squares and adds numbers in a list
# <Chad Hobbs>

def squareEach(nums): # A function that will square a number in a list
    for r in range(5):
        nums[r] = nums[r] ** 2
    print("The numbers that you entered all squared is:",nums)

def sumList(nums): # A function that will sum all of the numbers in the list
    sumup = 0
    for r in range(5):
        sumup = sumup + nums[r]
    print("The numbers that you entered all summed is:",sumup)

def main(): # Main program
    a,b,c,d,e = eval(input("Please input five numbers that will be squared, separated by commas(ie: 1,2,3,4,5): "))
    nums = [a,b,c,d,e]
    sumList(nums)
    squareEach(nums)
    
    

main()


    
