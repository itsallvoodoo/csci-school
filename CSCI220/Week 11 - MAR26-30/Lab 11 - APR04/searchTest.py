#Code compares runtimes of linear and binary search

from algorithms import *
import time

def main():
    print("Code to look at runtime for linear vs. binary search.")
    data = readData("dataSorted.txt")
    numDig = 5 #number of digits to output

    #small list of information
    print("\n" + "-" * 10)
    print("\nList with " + str(len(data)) + " elements.\n")
    
    print("Find 57 - beginning of list")
    start = time.time()
    isInLinear(57, data)
    end = time.time()
    print("Linear ->  " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(57, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind 158 - middle of list")
    start = time.clock()
    isInLinear(158, data)
    end = time.clock()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(158, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind 282 - end of list")
    start = time.clock()
    isInLinear(282, data)
    end = time.clock()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(282, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind 1 - not in list")
    start = time.time()
    isInLinear(1, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(1, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    #Number of elements in the list is a bit over 'last'
    last = 10000951 #adds integers between 1000 and 'last' to end of list
    data = data + list(range(1000, last))
    print("\n" + "-" * 10)
    print("\nList with " + str(len(data)) + " elements.\n")
    
    print("Find 57 - beginning of list")
    start = time.time()
    isInLinear(57, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(57, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind 500000 - middle of list")
    start = time.time()
    isInLinear(500000, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(500000, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")
    
    print("\nFind " + str(last) + " - end of list")
    start = time.time()
    isInLinear(last, data)
    end = time.time()
    print("Linear - " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(last, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

    print("\nFind 1 - not in list")
    start = time.time()
    isInLinear(1, data)
    end = time.time()
    print("Linear -> " + str(round(end - start, numDig)) + " seconds.")

    start = time.time()
    isInBinary(1, data)
    end = time.time()
    print("Binary -> " + str(round(end - start, numDig)) + " seconds.")

main()
