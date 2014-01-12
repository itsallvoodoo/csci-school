/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Dr. Bowring
 * 
 * Driver exercises the SortedArray with StudentListing nodes.
 */
package p2_Soln;

/**
 *
 * @author James F. Bowring
 */
public class Driver {

    /**
     * Full testing is left as an exercise for the student.
     * @param args the command line arguments
     */
    public static void main ( String[] args ) {

        int studentCount = 3;
       
        SortedArray studentListings = new SortedArray( studentCount );
        studentListings.showAll();

        for (int i = 0; i < studentCount; i ++) {
            StudentListing studentListing = new StudentListing();
            studentListing.inputNode();

            if (  ! studentListing.hasDefaultKey() ) {
                studentListings.insert( studentListing );
                studentListings.insert( studentListing );
            }
        }

        studentListings.showAll();

        String fetchKey = "a";
        KeyFieldInterface fetchedListing = studentListings.fetch( fetchKey );

        if ( fetchedListing instanceof StudentListing ) {
            System.out.println( "Fetch and then delete using key = " + fetchKey + ":\n" + fetchedListing.toString() );
            
            studentListings.delete( fetchKey);
            studentListings.showAll();
            
        } else {
            System.out.println( "Listing with key " + fetchKey + " not found." );
        }
        
        //test update
        StudentListing updatedNode = new StudentListing( "wasB", "3", "3");
        System.out.println(studentListings.update( "b", updatedNode));
        studentListings.showAll();
    }
}
