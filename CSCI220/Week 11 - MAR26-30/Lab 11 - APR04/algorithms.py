# algorithms.py
# This is all about searches and sorts
# Binary search is definitely faster than Linear search
# Python's built in sort is ridiculously faster than Selection, 2nd, and Insertion, 3rd, but Selection is only around 30% faster.
# <Chad Hobbs>

def readData(filename):
    numbers = []
    infile = open(filename,"r")
    lines = infile.readlines()
    for i in range(len(lines)):
        line = lines[i].strip().split(" ")
        for j in range(len(line)):
            numbers.append(int(line[j]))
    infile.close()
    return numbers

def isInLinear(srchValue, values):
    for i in range(len(values)):
        if srchValue == values[i]:
            return True
    return False
    
def isInBinary(srchValue, values):
    iMin = 0
    iMid = len(values)/2
    iMax = len(values)
    while True:
        iMid = int((iMax+iMin)/2)
        if values[iMid] < srchValue:
            iMin = iMid+1
        elif values[iMid] > srchValue:
            iMax = iMid-1
        else:
            return True
        if iMid == iMin or iMid == iMax:
            return False

def bubbleSort(values):
    print("Bubblesort before")
    print(values)
    switch = True
    while switch:
        switch = False
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                values[i],values[i+1] = values[i+1],values[i]
                switch = True
    print("Bubblesort after")
    print(values)
    return              
            
def insertionSort(values):
    print("Insertion before")
    print(values)
    for i in range(1, len(values)):
        key = values[i]
        j = i
        while j > 0 and values[j - 1] > key:
            values[j] = values[j - 1]
            j = j - 1
        values[j] = key
    return values

def selectionSort(values):
    print("Selection before")
    print(values)
    for i in range(0, len (values)):
        min = i
        for j in range(i + 1, len(values)):
            if values[j] < values[min]:
                min = j
        values[i], values[min] = values[min], values[i]
    print("Selection after")
    print(values)
    return

def main():
    file = "dataSorted.txt"
    nums = readData(file)
    
    # Search area------------------------
    entry = eval(input("Enter a number to search for: "))
    
    cond = isInLinear(entry,nums)
    if cond:
        print("Your number was found via Linear search!")
    else:
        print("Your number was not found via Linear search.:(")

    cond = isInBinary(entry,nums)
    if cond:
        print("Your number was found via Binary search!")
    else:
        print("Your number was not found via Binary search.:(")

    # Sort area---------------------------

    file = "dataUnsorted.txt"
    nums = readData(file)
    bubbleSort(nums)

    nums = readData(file)
    values = insertionSort(nums)
    print("Insertion after")
    print(values)

    nums = readData(file)    
    selectionSort(nums)
    

main()
