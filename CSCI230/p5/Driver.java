/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 02OCT12
 * 
 * Driver exercises the SLLQueue Class to create a queue with implementing a doubly-
 * linked list.
 * 
 */
package p5;

/**
 *
 * @author chadhobbs
 */

public class Driver {
    

    public static void main ( String[] args ) {
        
        // Testing whether or not the Queue has been created
        SLLQueue myQueue = new SLLQueue();
        if (myQueue != null) {
            System.out.println("Queue initialized: true");
        } else {
            System.out.println("Queue initialized: false");
        }
        
        // Attempting to insert 1 entry
        if (myQueue.insert(new Listing("Chad","Pine St","123"))) {
            System.out.println("Successfully inserted Entry 1: Chad, Pine St, 123");
        } else {
            System.out.println("Failed inserting Entry 1: Chad, Pine St, 123");
        }
        
        // Attempting to insert a 2nd entry
        if (myQueue.insert(new Listing("John","Oak St","456"))) {
            System.out.println("Successfully inserted Entry 2: John, Oak St, 456");
        } else {
            System.out.println("Failed inserting Entry 2: John, Oak St, 456");
        }
        
        // Attempting to insert a 3nd entry
        if (myQueue.insert(new Listing("Adam","Plum St","789"))) {
            System.out.println("Successfully inserted Entry 3: Adam, Plum St, 789");
        } else {
            System.out.println("Failed inserting Entry 3: Adam, Plum St, 789");
        }
        
        System.out.println("Show all:");
        myQueue.showAll();
        
        myQueue.delete();
        
        System.out.println("Deleted one, showing all:");
        myQueue.showAll();
        
        if (myQueue.delete()) {
            System.out.println("Successfully deleted first entry");
        } else {
            System.out.println("Failed to delete first entry");
        }
        
        // Attempting to insert a 4th entry
        if (myQueue.insert(new Listing("Ralph","Apple St","567"))) {
            System.out.println("Successfully inserted Entry 4: Ralph, Apple St, 567");
        } else {
            System.out.println("Failed inserting Entry 4: Ralph, Apple St, 567");
        }
        
        System.out.println("Deleted one, inserted new, showing all");
        myQueue.showAll();
        
        System.out.println("Fetching front:");
        Listing n = myQueue.fetch();
        if (n == null) {
            System.out.println("Returned null");
        } else {
            System.out.print("Returned: ");
            System.out.println(n.toString());
        }
        
        System.out.println("Testing complete.");
        
    }
    
    
}
