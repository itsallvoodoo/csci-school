
package p13;

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

