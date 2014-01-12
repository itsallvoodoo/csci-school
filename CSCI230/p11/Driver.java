/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 13NOV12
 * 
 * Driver exercises 8.39
 * 
 */
package p11;

/**
 * Description: This class uses a merge sort to demonstrate how the
 * merge sort works
 * 
 * pre-conditions: none
 * post-conditions: All methods have been tested.
 * 
 * @return 
 */
public class Driver {

    public static void main(String[] args) {
        
        runTest(1000);
        runTest(5000);
        runTest(10000);
        runTest(100000);
        
        System.out.println();
        System.out.println("Testing complete.");
        
    }
    
    public static void runTest(int x) {
        
        MergeSort aSort = new MergeSort();
        int[] mainArray = aSort.createArray(x);
        System.out.print("Testing sort method with array size: ");
        System.out.println(x);
        aSort.sort(mainArray);
        System.out.print("Comparisons: ");
        System.out.print(aSort.printComps());
        System.out.print(". Swaps: ");
        System.out.println(aSort.printSwaps());
        
        
        }
}


