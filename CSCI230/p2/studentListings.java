package p2;

/**
 * This class creates the database entry type and its associated methods.
 * @author chadhobbs
 */
public class studentListings implements Node {
    // name is key field

    private String name;
    private String studentID;
    private String GPA;

    public studentListings(String n, String id, String g) {
        name = n;
        studentID = id;
        GPA = g;
    }
    
    @Override
    public String toString() {
        return ("Name is " + name
                + "\nStudent ID is " + studentID
                + "\nGPA is " + GPA + "\n");
    }

    public Node deepCopy() {
        studentListings exactCopy = new studentListings(name, studentID, GPA);
        return exactCopy;
    }

    public int compareTo(Object targetKey) {
        String tKey = (String) targetKey;
        return (name.compareTo(tKey));
    }
    public String getKey() {return name;}
}
