/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 09OCT12
 * 
 * Driver exercises the DirectedHash class. Driver calls the methods of Directedhash
 * and tests their error-handling
 * 
 * pre-conditions: none
 * post-conditions: none
 * 
 */
package p6;

/**
 *
 * @author chadhobbs
 */

public class Driver {
    

    public static void main ( String[] args ) {
        
        
        DirectHashed dHash = new DirectHashed(100000,2000);
        
        System.out.println();
        System.out.println("Inserting ticket 2000: " + dHash.insert(new Listing("2000","Chad")));
        System.out.println();
        System.out.println("Inserting ticket 60000: " + dHash.insert(new Listing("60000","John")));
        System.out.println();
        System.out.println("Inserting ticket 3456: " + dHash.insert(new Listing("3456","Jill")));
        System.out.println();
        System.out.println("Inserting ticket 56777: " + dHash.insert(new Listing("56777","Tom")));
        System.out.println();
        System.out.println("Inserting ticket 12876: " + dHash.insert(new Listing("12876","Greg")));
        System.out.println();
        System.out.println("Inserting ticket 5: " + dHash.insert(new Listing("5","Brad")));
        System.out.println();
        System.out.println("Inserting ticket 1000000: " + dHash.insert(new Listing("1000000","Billy")));
        System.out.println();
        System.out.println("Fetching ticket 2000: " + dHash.fetch("2000"));
        System.out.println();
        System.out.println("Deleting ticket 2000: " + dHash.delete("2000"));
        System.out.println();
        System.out.println("Fetching ticket 2000: " + dHash.fetch("2000"));
        System.out.println();
        System.out.println("Fetching ticket 60000: " + dHash.fetch("60000"));
        System.out.println();
        System.out.println("Updating ticket 60000: " + dHash.update("60000",new Listing("60000","James")));
        System.out.println();
        System.out.println("Fetching ticket 60000: " + dHash.fetch("60000"));
        System.out.println();
        System.out.println("Printing all tickets");
        dHash.showAll();
        
        System.out.println();
        System.out.println("Testing complete.");
        
    }
    
    
}
