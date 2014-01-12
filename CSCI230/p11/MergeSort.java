/*
 * MergeSort.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 13NOV12
 * 
 *  Mergesort implements the required methods of exercise 8.39,
 * demonstrating a merge sort and displaying swaps and comparisons
 * 
 */
package p11;

import java.util.Random;

/**
 *
 * @author chadhobbs
 */
public class MergeSort {
    int swaps;
    int comparisons;
    
    public MergeSort() {
        swaps = 0;
        comparisons = 0;
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
    public int[] createArray(int x) {
        
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
     * Description: This method sorts a provided array and reports swaps
     * and comparisons.
     * 
     * Pre-conditions: An integer based array
     * Post-conditions: Array will be sorted with reporting
     * @param anArray 
     */
    public void sort(int[] numbers) {
        
        int[] temp = new int[numbers.length];
        mergeSort(numbers, temp, 0, numbers.length-1);
        
    }
    
    public void mergeSort(int items[], int temp[], int leftIndex, int rightIndex) {
        int midIndex, nItems;
        nItems = rightIndex - leftIndex + 1;
        if (nItems == 1) // base case
        {
            return;
        }
        midIndex = (rightIndex + leftIndex) / 2;
        mergeSort(items, temp, leftIndex, midIndex); // first reduced problem
        mergeSort(items, temp, midIndex + 1, rightIndex); // second reduced problem
        merge(items, temp, leftIndex, midIndex + 1, rightIndex); // general solution
    }

    public void merge(int items[], int temp[], int leftIndex, int midIndex, int rightIndex) {
        int leftEnd, nItems, tempsIndex;
        leftEnd = midIndex - 1;
        tempsIndex = leftIndex;
        nItems = rightIndex - leftIndex + 1;
        while ((leftIndex <= leftEnd) && (midIndex <= rightIndex)) { // move items into temp
            comparisons = comparisons + 1;
            if (items[leftIndex] <= items[midIndex]) { // move item from left sublist
            
                swaps = swaps + 1;
                temp[tempsIndex] = items[leftIndex];
                tempsIndex = tempsIndex + 1;
                leftIndex = leftIndex + 1;
            } else // move item from right sublist into temp
            {
                temp[tempsIndex] = items[midIndex];
                tempsIndex = tempsIndex + 1;
                midIndex = midIndex + 1;
            }
        }
        comparisons = comparisons + 1;
        if (leftIndex <= leftEnd) // left sublist is not empty
        {
            while (leftIndex <= leftEnd) { // copy remainder of left sublist to temp
                swaps = swaps + 1;
                temp[tempsIndex] = items[leftIndex];
                leftIndex = leftIndex + 1;
                tempsIndex = tempsIndex + 1;
            }
        } else // right sublist is not empty
        {
            while (midIndex <= rightIndex) { // copy remainder of right sublist into temp
                swaps = swaps + 1;
                temp[tempsIndex] = items[midIndex];
                midIndex = midIndex + 1;
                tempsIndex = tempsIndex + 1;
            }
        }
        for (int i = 0; i < nItems; i++) // copy temp into items
        {
            items[rightIndex] = temp[rightIndex];
            rightIndex = rightIndex - 1;
        }
    }
    public int printSwaps() {return swaps;}
    public int printComps() {return comparisons;}
}


