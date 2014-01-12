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
package p4;

/**
 *
 * @author chadhobbs
 */
interface Stack {

    public void push();

    public Node pop();

    public void peek();

    public void showAll();

    public void getTop();

    public void getSize();
}
