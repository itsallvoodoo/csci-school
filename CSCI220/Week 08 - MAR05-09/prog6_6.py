# prog6_6.py
# This program sums a list of numbers using functions
# <Chad Hobbs>


def sumList(nums): #function sums a list

    total = 0
    for i in range((len(nums))):
        total = total + nums[i]
    
    return total


def main(): # Main program
    initial = [2,3,4,5,6,7,8,9]
    print("The original list is",initial)

    final = sumList(initial)
    print("The sum of the list is",final)


main()
