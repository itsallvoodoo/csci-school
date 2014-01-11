import sys

def InsertionSort(array):
    i = 0
    j = 0
    n = len(array)
    for j in range(n):
        key = array[j]
        i = j - 1
        while (i >= 0 and array[i] > key):
            array[i + 1] = array[i]
            i = i -1
        array[i + 1] = key

def PrintArray(array):
    for x in range(len(array)):
        print(str(array[x]) + " ",end="")
    print()

def TestIntegerArray():
    iarr = [10,3,8,1,99,5,-1]
    PrintArray(iarr)
    InsertionSort(iarr)
    PrintArray(iarr)

def TestStringArray():
    sarr = ["Delhi","Sydney","California","Singapore"]
    PrintArray(sarr)
    InsertionSort(sarr)
    PrintArray(sarr)

if __name__ == "__main__":
    TestIntegerArray()
    TestStringArray()
