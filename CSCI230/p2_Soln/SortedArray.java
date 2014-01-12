/*
 * SortedArray.java
 * 
 * CSCI 230
 * Fall 2012
 * Dr. Bowring
 * 
 * SortedArray implements the DataStructureKeyFieldInterface for objects 
 * of any class that implements KeyFieldInterface.
 */
package p2_Soln;

/**
 *
 * @author James F. Bowring
 */
public class SortedArray implements DataStructureKeyFieldInterface {

    /**
     * Instantiate binarySearch object
     */
    private static final BinarySearch binarySearch = new BinarySearch();
    /**
     * count of nodes stored in data structure
     */
    private int elementCount;
    /**
     * data structure
     */
    private KeyFieldInterface[] data;
    /**
     * size of data structure
     */
    private int size;

    /**
     * Default constructor
     */
    public SortedArray () {
        this( 100 );
    }//end of constructor

    /**
     * Constructor specifying array size.
     *
     * @param s
     */
    public SortedArray ( int s ) {
        elementCount = 0;
        data = new KeyFieldInterface[s];
        size = s;
    }//end of constructor

    /**
     * Insert node if space available
     *
     * @param newListing
     * @return
     */
    @Override
    public boolean insert ( KeyFieldInterface newListing ) {

        boolean success = false;

        if ( elementCount == 0 ) {
            // empty data structure
            data[0] = newListing.deepCopy();
            success = true;

        } else if ( elementCount < size ) {
            // space to insert node is available
            int insertionPoint = binarySearch.binarySearchForInsertion( data, elementCount, newListing.getKey() );

            if ( insertionPoint >= 0 ) {
                // newListing key was not present, so insert node
                for (int j = elementCount; j > insertionPoint; j --) {
                    data[j] = data[j - 1];
                }

                data[insertionPoint] = newListing.deepCopy();
                success = true;
            } else {
                System.out.println( "DUPLICATE KEY" );
            }
        } else {
            System.out.println( "FULL DATA STRUCTURE" );
        }

        if ( success ) {
            elementCount ++;
        }

        return success;
    } // end of insert method

    /**
     * Retrieve deep copy of node if key present in data structure
     *
     * @param targetKey
     * @return
     */
    @Override
    public KeyFieldInterface fetch ( String targetKey ) {

        KeyFieldInterface target = null;

        if ( elementCount > 0 ) {
            int locationIndex = binarySearch.binarySearchForFetch( data, elementCount, targetKey );

            if ( locationIndex >= 0 ) {
                target = data[locationIndex].deepCopy();
            }
        }

        return target;

    }// end of the fetch method

    /**
     * Delete node if targetKey present in data structure.
     *
     * @param targetKey
     * @return
     */
    @Override
    public boolean delete ( String targetKey ) {

        boolean success = false;

        if ( elementCount > 0 ) {
            int locationIndex = binarySearch.binarySearchForFetch( data, elementCount, targetKey );

            if ( locationIndex >= 0 ) {
                // targetKey found
                elementCount --;

                int i = locationIndex;
                // move all elements after delete element up one position
                while (i < elementCount) {
                    data[i] = data[i + 1];
                    i ++;
                }
                // delete duplicate last element
                data[elementCount] = null;

                success = true;
            }
        }

        return success;
    }// end of delete method

    /**
     * Delete node with key == targetKey; insert newNode
     *
     * @param targetKey
     * @param newNode
     * @return
     */
    @Override
    public boolean update ( String targetKey, KeyFieldInterface newNode ) {

        boolean success = false;

        if ( delete( targetKey ) ) {
            success = insert( newNode.deepCopy() );
        }

        return success;
    }// end of update method

    /**
     *
     */
    public void showAll () {
        System.out.println( "\nListing\n" );
        for (int i = 0; i < elementCount; i ++) {
            System.out.println( data[i].toString() );
            System.out.println();
        }
    }// end of showAll method
}// end of class SortedArray

