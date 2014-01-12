/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p7;
import java.util.Arrays;

/**
 *
 * @author chadhobbs
 */
public class RecursionExercises {
    
    // SOLUTION TO 11c (17) - Product of 2 integers
    public static int exercise17(int a, int b) {
        
        return (b == 0) ? 0 : a + exercise17(a,b-1);
    }
    
    //SOLUTION to 11d (14) - Sum of two integers
    public static int exercise14(int a, int b) {
          
        if(a < b) {
            return 0;
        }
        else { 
            return a + exercise14(a - 1, b);
        }

    }
    
    //SOLUTION to 11e (15) Array of chars
    public static char[] exercise15(int start, int end) {
        char[] myArray = {'H','e','l','l','o','W','o','r','l','d'};
        
        
        if (start == end) {
            return null;
        } else {
            System.out.print(myArray[start]);
            return exercise15(start+1,end);
        }
    }
    
    //SOLUTION to 11f (16) - Binary search of an array
    public static int exercise16(int[] sortedArray, int aKey) {
        int min = 0;
        int max = sortedArray.length;
        return rBSearch(sortedArray,min,max,aKey);
        
    }
    
    
    public static int rBSearch(int[] sorted, int min, int max, int key) {
    
        if (min < max) {

            int mid = min + (max - min) / 2;
            if (key < sorted[mid]) {
                return rBSearch(sorted, min, mid, key);

            } else if (key > sorted[mid]) {
                return rBSearch(sorted, mid + 1, max, key);

            } else {
                return mid;
            }
        }
        return -1;
    }
    
    
    
    // EXPONENT SOLUTION JUST FOR FUN
    public static void hanoi(int n, int S, int D, int E) {

        if (n == 1) {
            System.out.println("Move 1 ring from tower " + S + " to tower " + D);
        }
        else { 
            hanoi(n-1, S, E, D);
            System.out.println("Move 1 ring from tower " + S + " to tower " + D);
            hanoi(n-1, E, D, S);
        }
        
    }
        
    
    
    
}
