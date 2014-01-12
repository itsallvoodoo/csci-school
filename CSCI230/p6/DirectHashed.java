/*
 * DirectedHash.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 09OCT12
 * 
 * DirectedHash provides the methods and parameters to construct and manipulate
 * a Direct Hashed data structure
 * 
 * 
 */
package p6;

/**
 *
 * @author chadhobbs
 */
public class DirectHashed {
    int N;
    int upper;
    int lower;
    Listing deleted;
    private Listing[] data;
     
    /**
     * Constructor for this class
     * 
     * pre-conditions: Requires an upper limit and lower limit
     * post-conditions: Constructs an array of type Listing
     * 
     * @param u
     * @param l 
     */
    public DirectHashed(int u, int l) {
        upper = u;
        lower = l;
        data = new Listing[u - l];
        
    }
    
    /**
     * Inserts new Listings into the hashtable
     * 
     * pre-conditions: Requires a Listing with a key that is within range
     * post-conditions: Hashtable will have new listing inserted, returns whether
     * this was successful or not
     * 
     * @param newListing
     * @return 
     */
    public boolean insert(Listing newListing) {
        int ip = (stringToInt(newListing.getKey()) - lower);
        
        if (ip > upper || ip < 0) {
            System.out.println("Key out of range"); // For testing ----------
            return false;
        }
        data[ip] = newListing.deepCopy();
        return true;
    }
    
    /**
     * Fetch returns a Listing if it is found in the hashtable
     * 
     * pre-conditions: Requires a valid key
     * post-conditions: Returns a deep copy of the listing that is found
     * 
     * @param targetKey
     * @return 
     */
    public Listing fetch(String targetKey) {
        int ip = (stringToInt(targetKey) - lower);
        
        if(data[ip] == null) {
            System.out.println("Nothing to return"); // For testing ----------
            return null;
        }
        else
            return data[ip].deepCopy();
    }
    
    /**
     * Delete sets an existing listing to null
     * 
     * pre-conditions: Requires a valid key in the hashtable
     * post-conditions: Returns true if key is found and successfully deleted, otherwise
     * returns false.
     * 
     * @param targetKey
     * @return 
     */
    public boolean delete(String targetKey) {
        int ip = (stringToInt(targetKey) - lower);
        
        if (data[ip] == null) {
            System.out.println("Nothing to delete"); // For testing ----------
            return false;
        }
        else {
            data[ip] = null;
            return true;
        }
    }
    
    /**
     * Update will change existing listing parameters
     * 
     * pre-conditions: Requires a valid key and new/updated Listing with matching key
     * post-conditions: Returns whether the update was successful or not
     * 
     * @param targetKey
     * @param newListing
     * @return 
     */
    public boolean update(String targetKey, Listing newListing) {
        if (!targetKey.equals(newListing.getKey())) {
            System.out.println("Key mismatch"); // For testing ----------
            return false;
        }
        
        if(delete(targetKey) == false) {
            System.out.println("Failed update(delete)"); // For testing ----------
            return false;
        }
        else if(insert(newListing) == false) {
            System.out.println("Failed update(insert)"); // For testing ----------
            return false;
        }
        return true;
    }
    
    /**
     * Showall prints all listings in hashtable
     * 
     * pre-conditions: None
     * post-conditions: None
     */
    public void showAll() {
        for(int i = 0; i < (upper - lower); i++) {
            if(data[i] != null && data[i] != deleted)
                System.out.println(data[i].toString());
        }
    }
    
    /**
     * StringtoInt is meant to change more complicated keys into index keys. Most
     * of the code is truncated for this example due to the simplicity of the
     * exercise. The extra code may be implmented for other hashtable types.
     * 
     * pre-conditions: Requires any key
     * post-conditions: Returns integer version of key
     * 
     * 
     * @param aKey
     * @return 
     */
    public static int stringToInt(String aKey) {
        /*
        int pk = 0;
        int n = 1;
        int cn = 0;
        char c[] = aKey.toCharArray();
        int grouping = 0;
        
        while (cn < aKey.length()) {
            grouping = grouping << 8;
            grouping = grouping + c[cn];
            cn = cn + 1;
            
            if(n == 4 || cn == aKey.length()) {
                pk = pk + grouping;
                n = 0;
                grouping = 0;
            }
            
            n = n + 1;
        }
        */
        
        return Integer.parseInt(aKey);
    }
    
}
