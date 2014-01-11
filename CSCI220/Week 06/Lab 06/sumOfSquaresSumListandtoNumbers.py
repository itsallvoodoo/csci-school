# sumOfSquaresSumListandtoNumbers.py
# This program will call functions that do various things to them in lists
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

def toLetters(nums): # A function that converts a number list into a number string list
    strList = ['','','','','']
    for r in range(5):
        if nums[r] == 0:
            strList[r] = "zero"
        if nums[r] == 1: 
            strList[r] = "one"
        if nums[r] == 2:
            strList[r] = "two"
        if nums[r] == 3:
            strList[r] = "three"
        if nums[r] == 4:
            strList[r] = "four"
        if nums[r] == 5:
            strList[r] = "five"
        if nums[r] == 6:
            strList[r] = "six"
        if nums[r] == 7:
            strList[r] = "seven"
        if nums[r] == 8:
            strList[r] = "eight"
        if nums[r] == 9:
            strList[r] = "nine"
    print("Your list of strings is",strList)
    return strList
        

def toNumbers(strList): # A function that will convert strings to numbers in a list
    for r in range(5):
        if strList[r] == "zero":
            strList[r] = 0
        if strList[r] == "one":
            strList[r] = 1
        if strList[r] == "two":
            strList[r] = 2
        if strList[r] == "three":
            strList[r] = 3
        if strList[r] == "four":
            strList[r] = 4
        if strList[r] == "five":
            strList[r] = 5
        if strList[r] == "six":
            strList[r] = 6
        if strList[r] == "seven":
            strList[r] = 7
        if strList[r] == "eight":
            strList[r] = 8
        if strList[r] == "nine":
            strList[r] = 9
    return strList


def main(): # Main program
    a,b,c,d,e = eval(input("Please input five numbers, separated by commas(ie: 1,2,3,4,5): "))
    nums = [a,b,c,d,e]
    strList = toLetters(nums)
    sumList(nums)
    squareEach(nums)
    strList = toNumbers(strList)
    print("The list of these numbers as strings is",strList)

main()
