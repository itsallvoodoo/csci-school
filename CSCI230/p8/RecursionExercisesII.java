/*
 * RecursionExercisesII.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 23OCT12
 * 
 * RecursionExercisesII displays the path and value of an optimal way to traverse a given board.
 * 
 * pre-conditions: none
 * post-conditions: none
 * 
 */
package p8;

/**
 * 
 * @author chadhobbs
 */
public class RecursionExercisesII {
    
    // PARAMETERS
    int col = 0;
    int row = 9;
    int[] path = new int[10];
    board b = new board();
    
    /**
     * Description: This method iterates through 10 ending positions to find
     * the minimum path to the top row.
     * 
     * Pre-conditions: none
     * Post-conditions: If a lower toll is not found, returns false, otherwise
     * returns true that a minimum path has been found.
     * @return 
     */
    public void produceRoute() {
        
        int cheapestToll = 100;
        int[] cheapestPath = new int[10];
        int toll;
        
        for(int x = 0;x<10;x++) {
            
            
            System.out.print("Navigating to position [10][");
            System.out.print(x+1);
            System.out.println("]");
            toll = minToll(9,x);
            System.out.print("Minimum toll: ");
            System.out.println(toll);
            
            if (cheapestToll > toll) {
                cheapestToll = toll;
                System.arraycopy(path,0,cheapestPath,0,10);
            }
            System.out.println("-------------------------------------------");
        }
        
        System.out.println("A minimal path to take is: ");
        System.out.print("Beginning: ");
        for (int y=0;y < cheapestPath.length;y++) {
            System.out.print("[");
            System.out.print(y+1);
            System.out.print("][");
            System.out.print(cheapestPath[y]+1);
            System.out.print("],");
        }
        System.out.println("End");
        System.out.print("It costs: ");
        System.out.println(cheapestToll);

    }
    
    /**
     * Description: minToll recursively searches through an array to find the 
     * minimum cost path from a top column to a bottom column.
     * 
     * Pre-conditions: A start position in the array must be specified. Validity will
     * be checked.
     * Post-conditions: A final value for an optimal path.
     * 
     * Base Case: minToll[i][j]
     * Reduced case: minimum of (minToll[i-1][j-1], minToll[i-1][j], minToll[i-1][j+1])
     * General Solution: minToll[i][j] + minimum of (minToll[i-1][j-1], minToll[i-1][j], minToll[i-1][j+1])
     * @param i
     * @param j
     * @return 
     */
    private int minToll(int i, int j) {

        if (b.isValid(i,j)) {
            if (minToll(i-1,j-1) < minToll(i-1,j) && minToll(i-1,j-1) < minToll(i-1,j+1)) {
                path[i]=j;
                return b.getValue(i,j) + minToll(i-1,j-1);
            } else if (minToll(i-1,j) < minToll(i-1,j-1) && minToll(i-1,j) < minToll(i-1,j+1)) {
                path[i]=j;
                return b.getValue(i,j) + minToll(i-1,j-1);
            } else {
                path[i]=j;
                return b.getValue(i,j) + minToll(i-1,j+1);
            }  
        } else if (i == -1){
            return 0;
        }
        else {
            return 99;
        }
    }
}
