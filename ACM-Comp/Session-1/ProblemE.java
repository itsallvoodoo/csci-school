/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package probleme;

import java.util.Scanner;

/**
 *
 * @author chadhobbs
 */
public class ProblemE {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        
        String[][] storage = new String[100][25];
        
        String guess = in.nextLine();
        
        String[] values = guess.split(" ");
        
        int i = 0;
        while (!"0".equals(values[0])) {
            System.arraycopy(values, 0, storage[i], 0, values.length);
            guess = in.nextLine();
            values = guess.split(" ");
            i = i+1; 
        }
        i = 0;
        while (!"0".equals(storage[i][0])) {
            
            if(storage[i][0] == null) {break;}
            
            System.out.print(storage[i][1]);
            System.out.print(" ");
            
            for(int j=2;j<24;j++) {
                
                if(storage[i][j] == null) {break;}
                
                if(storage[i][j] == null ? storage[i][j-1] != null : !storage[i][j].equals(storage[i][j-1])) {
                    
                    System.out.print(storage[i][j]);
                    System.out.print(" ");
                }
                
            }
            System.out.println("$");
            i = i+1;
            
            
        }
        
        
    }
}
