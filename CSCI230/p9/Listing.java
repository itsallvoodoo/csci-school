/*
 * Listing.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 30OCT12
 * 
 * Listing creates an object and provides getters and setters to access a listing node
 * 
 * pre-conditions: none
 * post-conditions: none
 * 
 */
package p9;

public class Listing { 
    
    private String name;
    private String address;
    private String number;
    
    /**
     * 
     * @param n
     * @param a
     * @param num 
     */
    public Listing(String n, String a, String num ) {
       name = n;
       address = a;
       number = num;
  }
   
   public String toString( ) {
       return("Name is " + name +
        "\nAddress is " + address +
        "\nNumber is " + number + "\n");
   }
   
   public Listing deepCopy( ) {
       Listing clone = new Listing(name, address, number);
       return clone;
   }
   
   public int compareTo(String targetKey) { return(name.compareTo(targetKey)); }
   public void setAddress(String a) {  address = a; }
   public String getKey() {return name;}
   
 }


