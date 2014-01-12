/*
 * StudentListing.java
 * 
 * CSCI 230
 * Fall 2012
 * Dr. Bowring
 * 
 * StudentListing implements the KeyFieldInterface for use with SortedArray.
 */
package p2_Soln;

import javax.swing.JOptionPane;

/**
 *
 * @author James F. Bowring
 */
public class StudentListing implements KeyFieldInterface {

    /**
     * Key field
     */
    private String name;
    /**
     * Stored as a string since will not be used as a number
     */
    private String identificationNumber;
    /**
     * Stored as a string since will not be used as a number
     */
    private String gradePointAverage;
    /**
     * Provides default key field value to denote the object s a place-holder.
     */
    public static final String DEFAULT_KEY_VALUE = "DEFAULT_NAME";

    /**
     * Default constructor.
     */
    public StudentListing () {
        this(DEFAULT_KEY_VALUE, "0", "0");
    }

    /**
     * Full constructor
     * @param name
     * @param identificationNumber
     * @param gradePointAverage 
     */
    public StudentListing ( String name, String identificationNumber, String gradePointAverage ) {
        this.name = name;
        this.identificationNumber = identificationNumber;
        this.gradePointAverage = gradePointAverage;
    }

    /**
     * Provides summary of fields for testing purposes.
     * @return 
     */
    @Override
    public String toString () {
        return ("Name is " + name
                + "\nIdentification number is " + identificationNumber
                + "\nGrade point average is " + gradePointAverage + "\n");
    }

    /**
     * Provides a deep copy of the object.
     * @return 
     */
    @Override
    public StudentListing deepCopy () {
        StudentListing clone = new StudentListing( name, identificationNumber, gradePointAverage );
        return clone;
    }

    /**
     * Returns the field used as the key.
     * @return 
     */
    @Override
    public String getKey () {
        return name;
    }
    
    /**
     * Detects whether the object has the default key.
     * @return 
     */
    @Override
    public boolean hasDefaultKey(){
        return name.equalsIgnoreCase( DEFAULT_KEY_VALUE);
    }

    /**
     * 
     */
    public void inputNode () {
        String inputValue = JOptionPane.showInputDialog( "Enter a name" );
        if ( (inputValue != null) && ( ! inputValue.trim().equals( "" )) ) {
            name = inputValue.trim();
        }

        if ( inputValue != null ) {
            inputValue = JOptionPane.showInputDialog( "Enter an Identification number" );
            if ( (inputValue != null) && ( ! inputValue.trim().equals( "" )) ) {
                identificationNumber = inputValue;
            }
        }

        if ( inputValue != null ) {
            inputValue = JOptionPane.showInputDialog( "Enter a Grade point average" );
            if ( (inputValue != null) && ( ! inputValue.trim().equals( "" )) ) {
                gradePointAverage = inputValue;
            }
        }
    }
}
