# prog6_5.py
# This program modifies a list of numbers by squaring the contents
# <Chad Hobbs>


def squareEach(nums): #function that takes a list of numbers and squares the contents

    for i in range((len(nums))):
        nums[i] = nums[i] ** 2
    
    return nums


def main(): # Main program
    initial = [2,3,4,5,6,7,8,9]
    print("The original list is",initial)

    final = squareEach(initial)
    print("The final list is",final)


main()
