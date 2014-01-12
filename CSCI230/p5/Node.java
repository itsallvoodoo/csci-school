/*
 * Node.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 02OCT12
 * 
 * The Node class is a structure that defines the basic building block of a list,
 * queue, stack, array, etc.
 * 
 */
package p5;

/**
 *
 * @author chadhobbs
 */


/**
 * The node class generates a node and provides getters and setters for the node.
 * 
 * Pre-conditions: none
 * Post-conditions: A node is created with two fields, Listing and Next
 * 
 * param
 */
public class Node {

    private Listing l;
    private Node next;

    public Node() {
    }
    
    public void setL (Listing L) {this.l = L;}
    public Listing getL () {return this.l;}
    public void setNext (Node N) {this.next = N;}
    public Node getNext () {return this.next;}
    
}
