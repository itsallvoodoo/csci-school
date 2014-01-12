/*
 * GenericQueueInterface.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 02OCT12
 * 
 * The Generic Queue Interface provides a description of the SLLQueue framework
 * 
 */
package p5;

/**
 * Specifies Queue operations
 * 
 * Pre-conditions: none
 * Post-conditions: none
 * 
 * @author chadhobbs
 */
public interface GenericQueueInterface {
    
    boolean insert(Listing newListing);
    
    Listing fetch();
    
    boolean delete();
    
    boolean update(String targetKey, Listing newListing);
    
    void showAll();
    
    
    
}
