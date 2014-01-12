/*
 * BinarySearchTree.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 30OCT12
 * 
 * This class is an implementation of a Binary Tree, and provides methods
 * to insert, fetch, and scan the tree.
 * 
 * pre-conditions: Listing class
 * post-conditions: A binary search tree with possible nodes
 * 
 */
package p9;

/**
 *
 * @author chadhobbs
 */
public class BinarySearchTree implements BinaryTree {
    
    Listing[] mainTree;
    Listing empty = new Listing("empty","","");
    
    
    /**
     * * Description: This method is the default constructor, it calls another
     * constructor with a node parameter
     * 
     * Pre-conditions: none
     * Post-conditions: none
     */
    public BinarySearchTree() {
        this(5);
    }
    
    /**
     * * Description: This method creates an array of nodes which provides
     * the framework for a binary search tree.
     * 
     * Pre-conditions: Number of nodes
     * Post-conditions: An array of Listings of length nodes.
     * @param nodes 
     */
    public BinarySearchTree(int nodes) {
        
        
        mainTree = new Listing[nodes];

    }
    
    /**
     * * Description: This method searches the tree to find a Listing key 
     * that matches the provided string.
     * 
     * Pre-conditions: A string
     * Post-conditions: Returns a matching Listing or an empty Listing.
     * 
     * @param targetKey
     * @return 
     */
    public Listing fetch(String targetKey) {
        return this.fetch(0,targetKey);
    }
     
    /**
     * * Description: This method searches the tree to find a Listing key 
     * that matches the provided string, given the starting array position.
     * 
     * Pre-conditions: A string and an integer representing a position in the tree array.
     * Post-conditions: Returns a matching Listing or an empty Listing.
     * 
     * @param node
     * @param targetKey
     * @return 
     */
    public Listing fetch(int node, String targetKey) {
        
        if (node <= mainTree.length) {
            if (mainTree[node] == null) {
                return empty;
            }
            //System.out.print("Comparing ");
            //System.out.print(mainTree[node].getKey());
            //System.out.print(" and ");
            //System.out.println(targetKey);
            if (mainTree[node].getKey().compareTo(targetKey) == 0) {
                return mainTree[node];
            } else if (mainTree[node].getKey().compareTo(targetKey) > 0) {
                return fetch(node * 2 + 1, targetKey);
            } else {
                return fetch(node * 2 + 2, targetKey);
            }
        } else {
            return empty;
        }

    }
    
    /**
     * * Description: This method attempts to insert a given Listing into the array
     * tree, and either succeeds or fails due to copy or out of room in array.
     * 
     * Pre-conditions: A Listing
     * Post-conditions: Inserts Listing into array or returns reasons it couldn't.
     * 
     * @param newListing
     * @return 
     */
    public boolean insert(Listing newListing) {
        
        return this.insert(0,newListing);
        
    }
    
    /**
     * * Description: This method attempts to insert a given Listing into the array
     * tree, and either succeeds or fails due to copy or out of room in array,
     * given a starting position in the array tree.
     * 
     * Pre-conditions: A Listing and an integer representing a position in the array.
     * Post-conditions: Inserts Listing into array or returns reasons it couldn't.
     * 
     * @param node
     * @param newListing
     * @return 
     */
    public boolean insert(int node, Listing newListing) {
        
        if (node <= mainTree.length) {

            if (mainTree[node] == null) {
                mainTree[node] = newListing;
                return true;
            } else if (newListing.compareTo(mainTree[node].getKey()) < 0) {
                return insert(node * 2 + 1, newListing);
            } else if (newListing.compareTo(mainTree[node].getKey()) > 0) {
                return insert(node * 2 + 2, newListing);
               
            } else {
                System.out.print("Node already exists, ");
                return false;
            }
        } else {
            System.out.print("Array not large enough, ");
            return false;
        }
    }
    
    /**
     * * Description: This method searches the entire binary tree and returns
     * results in a pre-order listing.
     * 
     * Pre-conditions: Starting node, usually 0.
     * Post-conditions: None.
     * 
     * @param node 
     */
    public void scanNLR(int node){

        if (node > 15 || mainTree[node] == null) { return;}
        else {System.out.println(mainTree[node].getKey());}
        scanNLR(node*2+1);
        scanNLR(node*2+2);
        
    }     
}
