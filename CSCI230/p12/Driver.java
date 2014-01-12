/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 20NOV12
 * 
 * Driver exercises 9.35
 * 
 */
package p12;

/**
 * Description: This class tests the SimpleGraph class and its expandable
 * graph function.
 * 
 * pre-conditions: none
 * post-conditions: All methods have been tested.
 *  
 */
public class Driver {
    
    public static void main(String[] args) {
        
        System.out.println("Testing a dynamically expanded graph");
        
        System.out.println("Graph size starts out as 1 node");
        
        SimpleGraph flyUS = new SimpleGraph(1); // originally 5
        
        Listing v0 = new Listing("Philadelphia");
        Listing v1 = new Listing("New York");
        Listing v2 = new Listing("Boston");
        Listing v3 = new Listing("Los Angeles");
        Listing v4 = new Listing("Houston");
      // add the hub cities to the graph as vertices
        System.out.println("Inserting node: Philadelphia");
        flyUS.insertVertex(0, v0);
        System.out.println("Inserting node: New York");
        flyUS.insertVertex(1, v1);
        System.out.println("Inserting node: Boston");
        flyUS.insertVertex(2, v2);
        System.out.println("Inserting node: Los Angeles");
        flyUS.insertVertex(3, v3);
        System.out.println("Inserting node: Houston");
        flyUS.insertVertex(4, v4);
      // add the routes to the graph as edges
        flyUS.insertEdge(0,1);
        flyUS.insertEdge(0,3);
        flyUS.insertEdge(1,2);
        flyUS.insertEdge(1,3);
        flyUS.insertEdge(2,1);
        flyUS.insertEdge(3,4);
        flyUS.insertEdge(4,0);
        flyUS.insertEdge(4,3);
      // output the hubs and the routes stored in the graph
        System.out.println("");
        System.out.println("");
        for(int i=0; i<5; i++)
        {   System.out.print("hub " + i + "\'s ");
            flyUS.showVertex(i);
            System.out.println("its routes are: ");
           flyUS.showEdges(i);
        }
        
        System.out.println("Testing complete.");
  }
}

