/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package acmcodecomp;

import java.util.Scanner;

/**
 *
 * @author chadhobbs
 */
public class ProblemC {
    
    public static void main(String[] args) {
        int a;
        String s;
        Scanner in = new Scanner(System.in);
        
        a = Integer.parseInt(in.nextLine());
        String[] storage = new String[a]; 
        
        
        for(int i = 0;i<a;i++) {
            storage[i] = in.nextLine();
            
        }
        System.out.println("Gnomes:");
        for(int i = 0;i<a;i++) {
            String[] values = storage[i].split(" ");
            if(Integer.parseInt(values[0]) < Integer.parseInt(values[1]) && Integer.parseInt(values[1]) < Integer.parseInt(values[2])) {
                System.out.println("Ordered");
            } else if (Integer.parseInt(values[0]) > Integer.parseInt(values[1]) && Integer.parseInt(values[1]) > Integer.parseInt(values[2])) {
                System.out.println("Ordered");
                
            }
            else {
                System.out.println("Unordered");
            }
            
            
        }
        
    }
}
