/*
 * BubbleSort.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 08NOV12
 * 
 * Bubblesort implements the required methods of exercise 8.34 and 8.35,
 * demonstrating a bubble sort and displaying swaps and comparisons
 * 
 */
package p10;

import java.util.Random;

/**
 *
 * @author chadhobbs
 */
public class HeapSort {
    
    
    public HeapSort() {
    }
    
    /**
     *
     * Description: This method is creates an integer array of size x and
     * fills it with random numbers from 0 to x-1.
     * 
     * Pre-conditions: An integer.
     * Post-conditions: An array of size x.
     *
     * @param x
     * @return 
     */
    public static int[] createArray(int x) {
        
        Random gen = new Random();
        
        int n;
        
        int[] unsorted = new int[x];
        
        for(int i=0;i<x;i++) {
            n = gen.nextInt(x);
            
            for(int j=0;j<i;j++) {
                if(unsorted[j] == n) {
                    n = gen.nextInt(x);
                    j = 0;
                }
            }
            unsorted[i] = n;   
                
            }  
        return unsorted;
        }
    
    /**
     * Description: This method displays the contents of an array.
     * 
     * Pre-conditions: An integer array
     * Post-conditions: none
     * @param anArray 
     */
    public static void printArray(int[] anArray){
        
        System.out.println("Array:");
        System.out.print("{");
        for(int i = 0; i < anArray.length;i++) {
            System.out.print(anArray[i]);
            if(i < anArray.length - 1) {
                System.out.print(",");
            }
        }
        System.out.println("}");
    }
    
    /**
     * Description: This method sorts a provided array.
     * 
     * Pre-conditions: An integer based array
     * Post-conditions: Array will be sorted
     * @param anArray 
     */
    public static void sort(int[] anArray) {
        
        int current = anArray.length;
        current = (current / 2) - 1;
        
        
        
        
    }
    
    /**
     * Description: This method sorts a provided array and also provides
     * swap and comparison statistics.
     * 
     * Pre-conditions: An integer based array.
     * Post-conditions: Array will be sorted
     * @param anArray 
     */
    public static void sortWithReport(int[] anArray) {
        
    }
}
