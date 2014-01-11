def main():
   array = [1, 7, 4, 9, 4, 7, 2, 3, 0, 8]
   print("Before sort:-")
   print(array)
   bubbleSort(array)
   print("After sort:-")
   print(array)
 
def bubbleSort(array):
   swapHappened = True
 
   while swapHappened:
      swapHappened = False
 
      for x in range(0, len(array)-1):
         if array[x] > array[x+1]:
            # Swap data
            array[x], array[x+1] = array[x+1], array[x]
            swapHappened = True
 
main()
