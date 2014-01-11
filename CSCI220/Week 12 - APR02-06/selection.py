# selection.py
# This is an selection sort example
# <Chad Hobbs>

def selection_sort(list2):
    for i in range(0, len (list2)):                     # Step through entire list
        min = i                                         # Minimum value equals outside range
        for j in range(i + 1, len(list2)):              # Step through everything above first loop incrementer
            if list2[j] < list2[min]:                   # If the compared number is lower than the minimum, make it the minimum
                min = j
        list2[i], list2[min] = list2[min], list2[i]     # After going through list, swap the outer list position number with the found lowest number
    return(list2)

def main():
    print("Insertion Sort")
    list1 = [4,7,3,2,9,0,4,2,1,6,7]
    print(list1)
    list2 = selection_sort(list1)
    print(list2)

main()
