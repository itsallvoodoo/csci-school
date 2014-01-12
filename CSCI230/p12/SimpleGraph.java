/*
 * SimpleGraph.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 20NOV12
 * 
 * SimpleGraph exercises 9.35
 * 
 */
package p12;

/**
 *
 * @author chadhobbs
 */

public class SimpleGraph {

    Listing vertex[];  //the reference to the vertex array
    int edge[][];  // reference to the adjacency matrix array
    int max, numberOfVertices;
    
    /**
    * Description: This is the constructor for the simple graph, creates
    * an array of type Listing that is the given size and an associated
    * edge array.
    * 
    * pre-conditions: none
    * post-conditions: Graph and associated objects have been created.
    *  
    */
    public SimpleGraph(int n) {
        vertex = new Listing[n]; // allocation of the vertex array
        edge = new int[n][n];   // adjacency matrix with all elements set to 0
        max = n;
        numberOfVertices = 0;
    }
    
    /**
    * Description: This method inserts a new vertex into the graph, expanding
    * the size if necessary.
    * 
    * pre-conditions: A graph exists, a correct vertexNumber is provided, and a 
    *   provided listing is well formed.
    * post-conditions: A vertex has been inserted into the graph.
    *  
    */
    public boolean insertVertex(int vertexNumber, Listing newListing) {
        if (vertexNumber >= max) {//the graph is full
            
            expandGraph();
            // return false;
        }
        vertex[vertexNumber] = newListing.deepCopy();
        numberOfVertices++;
        return true;
    }
    
    /**
    * Description: This method inserts an edge into the edge array.
    * 
    * pre-conditions: The associated vertices exist
    * post-conditions: The connection between vertices has been established if they exist.
    *  
    */
    public boolean insertEdge(int fromVertex, int toVertex) {
        if (vertex[fromVertex] == null || vertex[toVertex] == null) {// non-existent vertex
        
            return false;
        }
        edge[fromVertex][toVertex] = 1;
        return true;
    }

    /**
    * Description: This method displays the vertex.
    * 
    * pre-conditions: Vertex exists
    * post-conditions: none.
    *  
    */
    public void showVertex(int vertexNumber) {
        System.out.println(vertex[vertexNumber]);
    }

    /**
    * Description: This method displays associated edges.
    * 
    * pre-conditions: Vertex exists
    * post-conditions: none.
    *  
    */
    public void showEdges(int vertexNumber) {//edges emanating from vertexNumber
    
        for (int column = 0; column < numberOfVertices; column++) {
            if (edge[vertexNumber][column] == 1) {// there is an edge
            
                System.out.println(vertexNumber + "," + column);
            }
        }
    }
    
    /**
    * Description: This method will expand a graph by one.
    * 
    * pre-conditions: Vertex and edge graphs exist
    * post-conditions: Both graphs have been expanded in size by one.
    *  
    */
    public void expandGraph() {
        
        // make temps
        int arraySize = vertex.length;
        Listing[] tempVertex = vertex;
        int[][] tempEdge = edge;
        
        // expand existing arrays
        vertex = new Listing[arraySize + 1];
        edge = new int[arraySize + 1][arraySize + 1];
        max++;
        numberOfVertices = 0;
        
        // copy items from old array into new array
        for(int x=0;x < arraySize;x++) {
            // insert vertex if it exists in temp
            if(tempVertex[x] != null) {
                insertVertex(x,tempVertex[x]);
            }
            
            
            for(int y=0;y < arraySize;y++) {
                // insert edge if it exists
                if(tempEdge[x][y] == 1) {
                    insertEdge(x,y);
                }
            }
        }
        System.out.print("Array expanded to ");
        System.out.println(vertex.length);
    }
}// end of SimpleGraph class

