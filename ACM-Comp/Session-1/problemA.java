package acmcodecomp;

import java.util.Scanner;

/**
 *
 * @author chadhobbs
 */
public class problemA {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a;
        String s;
        
    Scanner in = new Scanner(System.in);
    
    //System.out.println("Number of names?: ");
    
    a = Integer.parseInt(in.nextLine());
    String[] storage = new String[a];
    
    for(int i = 0;i < a;i++) {
        storage[i] = in.nextLine();
        
    }
    
    for(int i = 0;i < a;i++) {
        
        //System.out.println("Name?: ");
        

        if(storage[i].charAt(0) == ' ' || storage[i].charAt(0) == '0' || storage[i].charAt(1) == '1' || storage[i].charAt(0) == '2' || storage[i].charAt(0) == '3' || storage[i].charAt(0) == '4' || storage[i].charAt(0) == '5' || storage[i].charAt(0) == '6' || 
                storage[i].charAt(0) == '7' || storage[i].charAt(0) == '8' || storage[i].charAt(0) == '9'){
            
        } else {
            System.out.print("Hello ");
            System.out.print(storage[i]);
            System.out.println("!");
        }
       
        
    }
    
    }
}
