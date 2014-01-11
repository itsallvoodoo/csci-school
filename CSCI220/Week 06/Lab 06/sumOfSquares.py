# sumOfSquares.py
# This program will call a function that will modify the contents by squaring them
# <Chad Hobbs>

def squareEach(nums): # A function that will square a number in a list
    for r in range(5):
        nums[r] = nums[r] ** 2
    print("The numbers that you entered all squared is:",nums)
    

def main(): # Main program
    a,b,c,d,e = eval(input("Please input five numbers that will be squared, separated by commas(ie: 1,2,3,4,5): "))
    nums = [a,b,c,d,e]
    squareEach(nums)
    

main()


    
