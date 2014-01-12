/*
 * DataStructureKeyFieldInterface.java
 * 
 * CSCI 230
 * Fall 2012
 * Dr. Bowring
 * 
 * DataStructureKeyFieldInterface specifies data structures' public methods.
 */
package p2_Soln;

/**
 *
 * @author James F. Bowring
 */
public interface DataStructureKeyFieldInterface {
    
    public KeyFieldInterface fetch ( String targetKey );
    
    public boolean insert ( KeyFieldInterface newListing );
    
    public boolean delete ( String targetKey );
    
    public boolean update ( String targetKey, KeyFieldInterface newNode );
    
}
