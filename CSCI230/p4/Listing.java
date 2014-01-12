package p4;

/**
 *
 * @author chadhobbs
 */
public class Listing {
    
    private String character;
    
    public Listing(String c) {
        character = null;
    }
    
    public String getListing() {
        return character;
    }
    
    public void setListing(String n) {
        character = n;
    }
    
    public Listing deepCopy() {
        Listing clone = new Listing(character);
        return clone;
    }
    
    
    
    /**
     * Provides a method to compare strings to one another
     * @param targetKey
     * @return 
     */
    public int compareTo(String targetKey) {
        String tKey = (String) targetKey;
        return (this.compareTo(tKey));
    }
}
