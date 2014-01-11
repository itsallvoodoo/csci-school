# 120123_Demonstration_Exercises.py
#
# For loops
#
# <Chad Hobbs>


def part1(): # Not a loop, physically typing out every time you want to print something

    num1 = eval(input("Number 1: "))
    num1 = eval(input("Number 2: "))
    num1 = eval(input("Number 3: "))
    return

def part2(): # Intro to using the FOR loop

    x = eval(input("How many loops would you like? "))


    for i in range(x):
        print(i+1)
        
    return

def part3(): # Using the start and step parts of FOR

    for i in range(10,1,-2):
        print (i)

    return

def part4(): # Accumulators

    x = eval(input("How many loops would you like? "))
    total = 0
    
    for i in range(1,x+1):
        num = eval(input("Number "+str(i)+": "))
        total += num
        print(total)

    return

def main(): # The main program
    # part1();
    # part2();
    # part3();
    part4();
    return

main()
