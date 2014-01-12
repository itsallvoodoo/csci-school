package p2;

/**
 * This class is the interface definition for studentListings.
 * 
 * @author chadhobbs
 */
public interface Node
{  public abstract Node deepCopy();

   public abstract int compareTo(Object targetKey);
   
   public abstract String toString();
   
   public abstract String getKey();
}
