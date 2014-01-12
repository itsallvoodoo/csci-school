/*
 * board.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 23OCT12
 * 
 * board for exercise 6.24
 * 
 * This class provides a board with values for each position, a method to return
 * each value, and a method to check whether or not a position is actually on
 * the board.
 * 
 */
package p8;

/**
 *
 * @author chadhobbs
 */
public class board {
    
    int[][] values  = {
            {0,3,5,6,1,2,7,1,9,4},
            {8,8,3,6,5,8,3,9,1,5},
            {6,4,3,8,7,1,2,4,7,4},
            {5,3,8,4,2,6,7,9,3,5},
            {1,6,3,2,1,4,3,3,7,9},
            {7,3,7,4,4,1,5,9,9,4},
            {1,8,6,6,8,4,8,3,8,2},
            {4,8,1,9,7,9,2,3,5,4},
            {9,1,4,7,3,6,8,6,1,4},
            {6,4,7,4,8,3,6,7,2,4}
    };
    
    /**
     * Description: Returns a value from the board.
     * 
     * pre-conditions: 2 valid parameters that are addresses on the board
     * post-conditions: Returns an integer
     * 
     * @param x
     * @param y
     * @return 
     */
    public int getValue(int x, int y) {return values[x][y];}
    
    /**
     * Description: Checks to make sure a given ordered pair would return
     * a value from the board
     * 
     * pre-conditions: 2 integers
     * post-conditions: Returns a boolean whether the integers are valid
     * or not
     * 
     * @param x
     * @param y
     * @return 
     */
    public boolean isValid(int x, int y) {
        if (x>-1 && x<10 && y>-1 && y < 10) {
            return true;
        } else {
            return false;
        }
            
    }  
}
