/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p1;

import java.util.Random;

/**
 *
 * @author chadhobbs
 */
public class binarySearch {
    
    
    // ********** METHODS ************ //
    public static int binarySearchCounter(int[] searchedArray) {
        Random randomGenerator = new Random();      
        int targetInt = 1 + randomGenerator.nextInt(65000);
        int loops = 0;
        int low = 0;
        int high = 64999;
        int i = (high + low) / 2;
        while (targetInt != searchedArray[i] && high != low){
            if(targetInt < searchedArray[i])
                high = i-1;
            else
                low = i+1;
            i = (high + low) / 2;
            loops++;
            
        }
        return loops;
    }
    
}
