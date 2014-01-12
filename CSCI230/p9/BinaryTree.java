/*
 * BinaryTree.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 30OCT12
 * 
 * This is the interface providing the framework for the Binary Search Tree
 * 
 */
package p9;

interface BinaryTree {
    
    public boolean insert(int node, Listing newListing);
    
    public Listing fetch(String targetKey);
    
    public Listing fetch(int node, String targetKey);
    
    public void scanNLR(int node);

}