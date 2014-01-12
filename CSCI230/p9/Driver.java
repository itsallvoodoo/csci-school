/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 30OCT12
 * 
 * Driver exercises 7.29
 * 
 */
package p9;

import java.util.Random;

/**
 * Description: This class creates a BinarySearchTree and tests all of
 * its methods.
 * 
 * pre-conditions: none
 * post-conditions: All methods have been tested.
 * 
 * @return 
 */
public class Driver {

    public static void main(String[] args) {
        
        Random gen = new Random( 432165439 );
        int n;
        Listing[] people =  new Listing[8];
        
        people[0] = new Listing("Adam","123 Apple St.", "001");
        people[1] = new Listing("Brad","456 Baker St.", "002");
        people[2] = new Listing("Chad","789 Carry St.", "003");
        people[3] = new Listing("Dean","012 Dodge St.", "004");
        people[4] = new Listing("Evan","345 Elope St.", "005");
        people[5] = new Listing("Finn","678 Fault St.", "006");
        people[6] = new Listing("Greg","901 Gorge St.", "007");
        people[7] = new Listing("Hank","234 Horry St.", "008");
        
        BinarySearchTree tree1 = new BinarySearchTree(15);
        
        
        // -------------------TESTING INSERT EXAMPLE -------------------------
        System.out.println("Testing insert function with randomly generated Listings.");
        System.out.println();
        for (int x = 0;x < 10;x++) {
            n = gen.nextInt(8);
            System.out.print("Inserting ");
            System.out.print(people[n].getKey());
            System.out.print(": ");
            if(tree1.insert(people[n])) {System.out.println("success!");}
            else {System.out.println("failed."); }
        }
        
        
        // -------------------TESTING FETCH EXAMPLE -------------------------
        System.out.println();
        System.out.println("Testing fetch function with randomly generated Listings.");
        System.out.println();
        for (int x = 0;x < 10;x++) {
            n = gen.nextInt(8);
            System.out.print("Fetching ");
            System.out.print(people[n].getKey());
            System.out.print(": ");
            if (tree1.fetch(people[n].getKey()).getKey().compareTo(people[n].getKey()) == 0) { System.out.println("success!"); }
        else {System.out.println("failed."); }
        }
        
        // -------------------TESTING SCAN EXAMPLE -------------------------
        System.out.println();
        System.out.println("Scanning Tree in pre-order:");
        System.out.println();
        
        tree1.scanNLR(0);
        
    }   
}
