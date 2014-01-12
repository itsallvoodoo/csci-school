/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 08NOV12
 * 
 * Driver exercises 8.34 and 8.35
 * 
 */
package p10;

/**
 * Description: This class uses a bubble sort to demonstrate how the
 * bubble sort works
 * 
 * pre-conditions: none
 * post-conditions: All methods have been tested.
 * 
 * @return 
 */
public class Driver {

    public static void main(String[] args) {
        
        int[] mainArray = BubbleSort.createArray(50);
        
        System.out.println("Testing sort method:");
        BubbleSort.printArray(mainArray);
        BubbleSort.sort(mainArray);
        BubbleSort.printArray(mainArray);
        
        mainArray = BubbleSort.createArray(50);
        System.out.println("Testing sort method with reporting:");
        BubbleSort.printArray(mainArray);
        BubbleSort.sortWithReport(mainArray);
        BubbleSort.printArray(mainArray);
        
        System.out.println();
        System.out.println("Testing complete.");
    }
}

