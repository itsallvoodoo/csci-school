/**
 * Stack.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 11SEP12
 * 
 * 
 * Stack provides the framework for a stack of objects.
 * 
 */
package p3;

/**
 *
 * @author chadhobbs
 */
public class Stack {
    
    private Object[] nodes;
    private int top;
    private int size;

    /**
     * Default Constructor
     * 
     */
    public Stack() {
        
        this(50);
        
    }
    /**
     * Full Constructor
     * @param s 
     */
    public Stack(int s) {
        
        top = -1;
        size = s;
        nodes = new Object[s];
        
    }
    
    /**
     * Push puts an object on the top of the stack as long as there is room
     * in the stack.
     * @param newObject
     * @return 
     */
    public boolean push(Object newObject) {
        if(top == size - 1)
            return false;
        else {
            top = top + 1;
            nodes[top] = newObject;
            return true;
        }
    }
    
    /**
     * Pop returns and removes the object on top of the stack as long as there
     * are items in the stack.
     * @return 
     */
    public Object pop() {
        int topLoc;
        if(top == -1)
            return null;
        else {
            topLoc = top;
            top = top - 1;
            return nodes[topLoc];
        }
    }
    
    /**
     * Peek returns the top item in the stack without deleting it as long
     * as there are items in the stack.
     * @return 
     */
    public Object peek() {
        int topLoc;
        if(top == -1)
            return null;
        else {
            return nodes[top];
        }
    }
    
    /**
     * showAll will show the entire contents of the stack without modification.
     */
    public void showAll() {
        for(int i = top; i >= 0; i--) {
        }
    }
    
    /**
     * getTop returns the value of the top of the stack.
     * @return 
     */
    public int getTop() {return top;}
    
    /**
     * getSize returns the size of the stack.
     * @return 
     */
    public int getSize() {return size;}
}

