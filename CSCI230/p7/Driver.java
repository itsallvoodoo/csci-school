/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 16OCT12
 * 
 * Driver exercises xxx
 * 
 * pre-conditions: none
 * post-conditions: none
 * 
 */
package p7;

/**
 *
 * @author chadhobbs
 */
public class Driver {

    public static void main(String[] args) {
        
        /*
                
        System.out.println("Exercise 14------------------------");
        for(int x=4;x<8;x++){
            System.out.println("Summation of 3 to " + x + ": " + RecursionExercises.exercise14(x,3));
        }
        
        System.out.println("Exercise 15------------------------");
        for(int x=0;x<6;x++){
            System.out.print(x + " through 10: " );
            RecursionExercises.exercise15(x,10);
            System.out.println();
        }
        
        System.out.println("Exercise 16------------------------");
        int[] sorted = {2,3,4,5,6,7,8,9};
        for(int x = 2;x<10;x++) {
            System.out.println("Finding " + x + " in array (2,3,4,5,6,7,8,9): " + RecursionExercises.exercise16(sorted, x));
        }
                
        System.out.println("Exercise 17------------------------");
        for(int x=3;x<8;x++){
            System.out.println(x + " times 6: " + RecursionExercises.exercise17(x,6));
        }
        
        */
        
        RecursionExercises.hanoi(5, 1, 2, 3);
        
        System.out.println ("Testing complete.");
        
    }

    
    
    
}
