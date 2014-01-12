package p1;
import java.util.Random;
import java.io.IOException;
import java.io.DataInputStream;

/**
 * This program takes an input n, and searches for n random numbers in an array of 65000 numbers.
 * The average amount of loops through the array searching for each number is returned.
 * Due: 28AUG12
 * @author chadhobbs
 */
public class Driver {
    /**
     *  @param args the command line arguments
     */
    
    public static void main(String[] args) {
        int arraySize = 65000;
        int[] nums = new int[arraySize];
        
        for (int y=0;y<65000;y++){
            nums[y] = y + 1;
        }
        
        int n = 0;
        n = getData("How many integers to be located?: ");
        
        int total = 0; // Total number of times the search has looped
        for(int x=0;x<n;x++){ // SEARCH ARRAY n NUMBER OF TIMES
            total = total + binarySearch.binarySearchCounter(nums);
        }
        double avg = (double) total / (double) n; // Average number of loops based on number of search terms
        System.out.println("The loop executed an average of "+ avg + " times.");
        System.out.println("Log base 2 of " + arraySize + ": " + Math.log(arraySize) / Math.log(2));
    }
    
    /**
     * Search algorithm that also returns the loop counter
     * @return
     */
    
   
    /**
     * Method grabs the user entry and returns the value entered
     * @param prompt
     * @return
     */
    public static int getData(String prompt) {
        System.out.print(prompt);
        int data = 0;
        DataInputStream mykb = new DataInputStream(System.in);

        try {
            data = Integer.parseInt(mykb.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return data;
    }
}
