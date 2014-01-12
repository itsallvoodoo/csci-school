package acmcodecomp;

import java.util.Scanner;

/**
 *
 * @author chadhobbs
 */
public class ACMCodeComp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a;
        String s;
    
    Scanner in = new Scanner(System.in);
    
    System.out.println("Number of names?: ");
    
    a = Integer.parseInt(in.nextLine());
    
    for(int i = 0;i < a;i++) {
        
        System.out.println("Name?: ");
        s = in.nextLine();

        if(s.charAt(0) == ' ' || s.charAt(0) == '0' || s.charAt(1) == '1' || s.charAt(0) == '2' || s.charAt(0) == '3' || s.charAt(0) == '4' || s.charAt(0) == '5' || s.charAt(0) == '6' || 
                s.charAt(0) == '7' || s.charAt(0) == '8' || s.charAt(0) == '9'){
            
        } else {
            System.out.print("Hello ");
            System.out.print(s);
            System.out.println("!");
        }
       
        
    }
    
    }
}
