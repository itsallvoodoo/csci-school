/*
 * SLLQueue.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 02OCT12
 * 
 * SLLQueue provides a framework for a Double Ended singly linked list with the
 * associated methods and parameters.
 * 
 */
package p5;

/**
 * 
 * @author chadhobbs
 */
public class SLLQueue implements GenericQueueInterface {

    private Node h;  // list header
    private Node r;  // list rear
    
    /**
     * Constructor for SLLQueue
     * 
     * Pre-conditions: none
     * Post-conditions: A queue with 2 nodes, header and rear
     */
    public SLLQueue() {
        // Create Header
        h = new Node();
        h.setL(null);
        h.setNext(null);
        
        // Create Rear
        r = null;
        
    }
    
    /**
     * insert adds a node to the end of the queue
     * 
     * Pre-conditions: A queue exists
     * Post-conditions: A node has been added to the queue
     * 
     * @param newListing
     * @return 
     */
    public boolean insert(Listing newListing) {
        Node n = new Node();
        if (n == null) // out of memory
        {
            return false;
        } else {
            
            if (r == null) { // Empty list
                n.setL(newListing);
                r = n;
                h.setNext(n);
                //TODO System.out.println("empty loop");
            } else {
                n.setL(newListing);
                r.setNext(n);
                r = n;
                //TODO System.out.println("populated loop");
            }
            return true;
        }
    }
    
    /**
     * fetch returns the first node in the queue
     * 
     * Pre-conditions: There is a node in the queue
     * Post-conditions: The first node is returned, the queue is not changed.
     * 
     * @return 
     */
    public Listing fetch() {
        if (h.getNext() == null) {
            return null;
        } else {
            Listing p = h.getNext().getL();
            //TODO h.setNext(h.getNext().getNext());
            return p;
        }
    }
    
    /**
     * delete removes the first node in the queue.
     * 
     * Pre-conditions: There is a node in the queue
     * Post-conditions: The first node has been removed and if no nodes are left
     * on the stack rear has been updated.
     * 
     * @return 
     */
    public boolean delete() {
        Node q = h;
        Node p = h.getNext();
        if (p != null) {
            q.setNext(p.getNext());
            if (p == r) { r = null;}
            return true;
        } else {
            return false;
        }
    }
    
    // TODO Figure out how to implement update if it is needed.
    /**
     * update is not currently implemented. 
     * 
     * Pre-conditions:
     * Post-conditions:
     * 
     * @param targetKey
     * @param newListing
     * @return 
     */
    public boolean update(String targetKey, Listing newListing) {
        if (delete() == false) {
            return false;
        } else if (insert(newListing) == false) {
            return false;
        }
        return true;
    }
    
    /**
     *  showAll iterates through entire queue and displays all nodes.
     * 
     * Pre-conditions:
     * Post-conditions:
     * 
     */
    public void showAll() {
        Node p = h.getNext();
        while (p != null) {
            System.out.println(p.getL().toString());
            p = p.getNext();
        }
    }
}
