/*
 * KeyFieldInterface.java
 * 
 * CSCI 230
 * Fall 2012
 * Dr. Bowring
 * 
 * KeyFieldInterface provides for a String keyField and a default key.
 */package p2_Soln;

/**
 * 
 * @author James F. Bowring
 */
public interface KeyFieldInterface  {

    /**
     * Returns key field of object.
     * @return 
     */
    public String getKey();
    
    /**
     * Returns true if object's key is a default value.
     * @return 
     */
    public boolean hasDefaultKey();
    
    /**
     * Provides for deep copy of object.
     * @return 
     */
    public StudentListing deepCopy ();
    
}
