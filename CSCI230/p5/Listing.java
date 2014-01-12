/*
 * Listing.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 02OCT12
 * 
 * xxx
 * 
 */
package p5;

/**
 *
 * @author chadhobbs
 */
public class Listing
{ private String name;
   private String address;
   private String number;
   public Listing(String n, String a, String num )
  {  name = n;
      address = a;
      number = num;
  }
   public String toString( )
   {   return("Name is " + this.name +
                    ", Address is " + this.address +
                    ", Number is " + this.number);
   }
   public Listing deepCopy( )
   {  Listing clone = new Listing(name, address, number);
      return clone;
   }
   public int compareTo(String targetKey)
   {  return(name.compareTo(targetKey));
   }
   public void setAddress(String a)
   {  address = a;
   }
 }