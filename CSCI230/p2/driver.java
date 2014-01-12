package p2;

/** 
 *  CSCI230 Programming Problem 2 (2.19 and 2.20)
 *  This program creates a database of student information and associated
 *  methods to access and manipulate the database. 
 * 
 * @author chadhobbs
 */
public class driver {

    public static void main(String[] args) {
        sorted COFC = new sorted(10);
        studentListings chad = new studentListings("Chad", "2122",
                "4.00");
        studentListings jill = new studentListings("Jill", "2123",
                "3.67");
        studentListings adam = new studentListings("Adam", "2124",
                "2.51");
        studentListings lauren = new studentListings("Lauren", "2125",
                "3.98");

        COFC.insert(chad);
        COFC.insert(jill);
        COFC.insert(adam);
        COFC.insert(lauren);
        
        System.out.println("Should be sorted:");
        COFC.showAll();
        
        System.out.println();
        System.out.println("Retrieving Jill, Chad, Lauren, Adam");
        System.out.println(COFC.fetch("Jill").toString());
        System.out.println(COFC.fetch("Chad").toString());
        System.out.println(COFC.fetch("Lauren").toString());
        System.out.println(COFC.fetch("Adam").toString());
    }
}