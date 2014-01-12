/*
 * Listing.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 09OCT12
 * 
 * Listing provides the framework for an entry into a list, array, hashtable, etc
 * 
 * 
 */
package p6;

/**
 *
 * @author chadhobbs
 */
public class Listing
{ private String key;
   private String name;
   
   public Listing() {
       this("0","none");
   }
   
   
   /**
    * 
    * @param k
    * @param n 
    */
   public Listing(String k, String n) {
       key = k;
       name = n;
  }
   
   /**
    * 
    * @return 
    */
   public String toString( ) {
       return("Seat Number: " + this.key + ", purchaser: " + this.name);
   }
   
   /**
    * 
    * @return 
    */
   public Listing deepCopy() {
       Listing clone = new Listing(key, name);
       return clone;
   }
   
   /**
    * 
    * @return 
    */
   public String getKey() {
       return this.key;
   }
 }