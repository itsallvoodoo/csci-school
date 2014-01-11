# insertion.py
# This is an insertion sort example
# <Chad Hobbs>


def insertion_sort(list2):
    for i in range(1, len(list2)):              # Outer loop steps through list starting at 1
        save = list2[i]                         # Store iteration in save variable
        j = i                                   # J is used to step backwards through the list
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
        list2[j] = save
    return list2


def main():
    print("Insertion Sort")
    list1 = [4,7,3,2,9,0,4,2,1,6,7]
    print(list1)
    list2 = insertion_sort(list1)
    print(list2)

main()
