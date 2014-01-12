/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 11SEP12
 * 
 * 
 * Driver executes the ArithmeticExpressionConversions class which is 
 * the solution to problems 3.21 and 3.24 in the textbook
 * 
 * PRE CONDITIONS
 * 
 * Number entries are integers.
 * Parenthesis must not be used as shorthand multiplication.
 * 
 * POST CONDITIONS
 * 
 * User entry will be re-formatted for easier handling, this will be displayed
 * for visual verification.
 * Post-fixed formatting will be displayed for visual verification.
 * The answer will be displayed as an integer.
 * 
 */

package p3;

import java.io.IOException;
import java.io.DataInputStream;


/**
 * @author chadhobbs
 */
public class Driver {

    public static void main(String[] args) {
        
        // TODO Test the stack
        
        ArithmeticExpressionConversions entry = new ArithmeticExpressionConversions();
        String in = getData("Please enter a mathematical operation. -1 to quit: ");
        
        /*
         * Loop until the user enters -1 to exit the program
         */
        while (in.compareTo("-1") != 0 ) {
            
            
            if (entry.processEntry(in)) {
                
                /*
                 * The string entered is cleaned up, spaces removed, etc.
                 */
                System.out.print("Entry processed: ");
                entry.printInput();
                
                /*
                 * Entry is converted to Postfixed notation and displayed
                 */
                System.out.println("Entry converted to postfix: " + entry.convertInfixToPostfix());
                System.out.print("Entry converted to: ");
                entry.printPostString();
                        
                 /*
                 * The Postfixed entry is evaluated and the answer displayed
                 */
                int answer = entry.evaluatePostfixExpression();
                System.out.println("The answer is " + String.valueOf(answer));
            }
        
            
            in = getData("Enter another mathematical operation. -1 to quit: ");
        }
        
        
    }
    
    /*
     * This method is a generic method to retrieve user input as a string
     */
    public static String getData(String prompt) {
        System.out.print(prompt);
        String data = "";
        DataInputStream mykb = new DataInputStream(System.in);

        try {
            data = mykb.readLine();
        } catch (IOException e) {
            System.out.println("Entry not valid.");
        }
        return data;
    }
    
    
}
