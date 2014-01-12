/*
 * BinarySearch.java
 *
 * CSCI 230
 * Fall 2012
 * Dr. Bowring
 * 
 * BinarySearch provides methods for specifying insertion indices and 
 * location indices for arrays of type KeyFieldInterface.
 */
package p2_Soln;

/**
 *
 * @author James F. Bowring
 */
public class BinarySearch {

    /**
     * From textbook Data Structures and Algorithms, p. 77
     *
     * Pre-conditions: searchArray is not null and has at least one element
     * searchArray is filled with KeyFieldInterface objects through elementCount - 1
     *
     * Post-conditions: returned int is positive index of insertion point for
     * targetKey if targetKey not found, else returned int is -1 denoting target
     * Key found and insertion not allowed.
     *
     * This implementation uses rounding up of i.5 when i is even, rounding down
     * otherwise to balance the halving of the array when the elementCount is even.
     *
     * @param searchArray
     * @param elementCount
     * @param targetKey
     * @return 
     */
    public int binarySearchForInsertion ( KeyFieldInterface[] searchArray, int elementCount, String targetKey ) {

        int low = 0;
        int high = elementCount - 1;

        int index = roundUpHalfEven( (double) (high + low) / 2.0 );

        // because of rounding, index will be 0 only when elementCount = 1
        if ( index > 0 ) {
            while ((low <= high) //
                    && (index > 0) //
                    &&  ! targetKey.equals( searchArray[index].getKey() )
                    &&  ! ((targetKey.compareTo( searchArray[index].getKey() ) < 0) //
                    && targetKey.compareTo( searchArray[index - 1].getKey() ) > 0)) {

                if ( targetKey.compareTo( searchArray[index].getKey() ) < 0 ) {
                    high = index - 1;
                } else {
                    low = index + 1;
                }

                index = roundUpHalfEven( (double) (high + low) / 2.0 );
            }

            // after while loop ends, check if targetKey is present at index and return -1 if true
            if ( targetKey.equals( searchArray[index].getKey() ) ) {
                index = -1;
            }// otherwise, if low>high, then we have reached the end and insertion occurs at the end 
            else if ( low > high ) {
                index = elementCount;
            }

        } // here, index = 0, so decide whether targetKey is inserted at position 0 or 1 or not at all
        else {
            if ( targetKey.compareTo( searchArray[0].getKey() ) > 0 ) {
                index = 1;
            } else if ( targetKey.equals( searchArray[index].getKey() ) ) {
                index = -1;
            }
        }

        return index;
    }

    /**
     * From textbook Data Structures and Algorithms, p. 25
     * 
     * Pre-conditions: searchArray is not null and has at least one element
     * searchArray is filled with KeyFieldInterface objects through elementCount - 1
     *
     * Post-conditions: returned int is positive index of targetKey if found, 
     * else returned int is -1 denoting targetKey not found.
     *
     * This implementation uses rounding up of i.5 when i is even, rounding down
     * otherwise to balance the halving of the array when the length is even.
     * 
     * @param searchArray
     * @param elementCount
     * @param targetKey
     * @return 
     */
    public int binarySearchForFetch ( KeyFieldInterface[] searchArray, int elementCount, String targetKey ) {

        int low = 0;
        int high = elementCount - 1;

        int index = roundUpHalfEven( (double) (high + low) / 2.0 );

        while ((low != high) //
                &&  ! targetKey.equals( searchArray[index].getKey() )) {

            if ( targetKey.compareTo( searchArray[index].getKey() ) < 0 ) {
                high = index - 1;
            } else {
                low = index + 1;
            }

            index = roundUpHalfEven( (double) (high + low) / 2.0 );
        }

        // not found
        if (  ! targetKey.equals( searchArray[index].getKey() ) ) {
            index = -1;
        }

        return index;
    }

    /**
     * Rounds up to nearest integer when integer part is even, otherwise rounds
     * down
     *
     * @param n
     * @return
     */
    private static int roundUpHalfEven ( double n ) {
        int retVal;
        if ( ((int) Math.floor( n )) % 2 == 0 ) {
            retVal = (int) Math.ceil( n );
        } else {
            retVal = (int) Math.floor( n );
        }

        return retVal;
    }
    
}
