/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p4;

/**
 *
 * @author chadhobbs
 */
public class Node {
    
    private Listing l;
    private Node next;
    
    public Node() {
        l = new Listing(null);
        next = null;
    }
    
    /**
     * Provides a method to compare strings to one another
     * @param targetKey
     * @return 
     */
    public int compareTo(Object targetKey) {
        String tKey = (String) targetKey;
        return (this.compareTo(tKey));
    }
    
    public void setNext(Node n) {
        next = n;
    }
    
    public Node getNext() {
        return next;
    }
    
    public void setL(Listing listing) {
        l = listing;
    }
    
    public Listing getL() {
        return l;
    }
    
}
