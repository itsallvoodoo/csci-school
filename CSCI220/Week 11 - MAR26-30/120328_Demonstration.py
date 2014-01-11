# 120328_Demonstration.py
# In class demonstrations
# <Chad Hobbs>

import sys

# ---------------------------Sorts --------------------------

# ----- Bubble Sort ------

def bubbleSort(array):
    
    times = 0
    swapHappend = True
    while swapHappend:
        for i in range(len(array)-1,0,-1):
            swapHappend = False
            for j in range(0,i):
                times = times + 1
                if array[j] > array[j+1]:
                    array[j],array[j+1] = array[j+1],array[j]
                    swapHappend = True
                    
    display(times,array)
    return 
    
# ------------------------- Insertion Sort ------------------------

def InsertionSort(array):
    i = 0
    j = 0
    n = len(array)
    times = 0
    for j in range(n):
        key = array[j]
        i = j - 1
        while (i >= 0 and array[i] > key):
            array[i + 1] = array[i]
            i = i -1
            times = times + 1
        array[i + 1] = key

    display(times,array)
    return

##def PrintArray(array):
##    for x in range(len(array)):
##        print(str(array[x]) + " ",end="")
##    print()
##
##def TestIntegerArray():
##    iarr = [10,3,8,1,99,5,-1]
##    PrintArray(iarr)
##    InsertionSort(iarr)
##    PrintArray(iarr)
##
##def TestStringArray():
##    sarr = ["Delhi","Sydney","California","Singapore"]
##    PrintArray(sarr)
##    InsertionSort(sarr)
##    PrintArray(sarr)
##
##if __name__ == "__main__":
##    TestIntegerArray()
##    TestStringArray()

    

# ------------------------- Selection Sort ------------------------

##def SelectionSort(array):
##
##
##
##    return times, array





# -------------------------- Main Program -------------------------


def display(iterations,array):
    
    print("After sort:-")
    print(array)
    print("It takes",iterations,"iterations to accomplish the task")
    return

def main():
    array = [1, 7, 4, 9, 4, 7, 2, 3, 0, 8]
    print("Before sort:-")
    print(array)

   
    bubbleSort(array)
    array = [1, 7, 4, 9, 4, 7, 2, 3, 0, 8]
    print("Before sort:-")
    print(array)
    InsertionSort(array)

 




























main()
