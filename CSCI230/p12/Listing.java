/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p12;

/**
 *
 * @author chadhobbs
 */
public class Listing
{  private String name;
    public Listing(String n)
   {  name=n;
   }
    public String toString()
    {  return("Name is " + name);
    }
    public Listing deepCopy()
   {  Listing clone = new Listing(name);
       return clone;
   }
}
