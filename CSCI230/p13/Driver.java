/*
 * Driver.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 
 * 
 * Driver exercises a spanning tree
 * 
 */
package p13;

/**
 * Description: xxx.
 * 
 * pre-conditions: xxx
 * post-conditions: xxx.
 *  
 */
public class Driver {
    
    public static void main(String[] args) {
        
        int numberOfVertices = 5;
        
        SimpleGraph flyUS = new SimpleGraph(numberOfVertices);
        Listing v0 = new Listing("Philadelphia");
        Listing v1 = new Listing("New York");
        Listing v2 = new Listing("Boston");
        Listing v3 = new Listing("Los Angeles");
        Listing v4 = new Listing("Houston");
      // add the hub cities to the graph as vertices
        flyUS.insertVertex(0, v0);
        flyUS.insertVertex(1, v1);
        flyUS.insertVertex(2, v2);
        flyUS.insertVertex(3, v3);
        flyUS.insertVertex(4, v4);
      // add the routes to the graph as edges
        flyUS.insertEdge(1,2,1);
        flyUS.insertEdge(0,1,8);
        flyUS.insertEdge(0,3,9);
        flyUS.insertEdge(1,3,3);
        flyUS.insertEdge(0,4,5);
        flyUS.insertEdge(3,4,2);
        
        /* output the hubs and the routes stored in the graph
        for(int i=0; i<5; i++) {
            System.out.print("hub " + i + "\'s ");
            flyUS.showVertex(i);
            System.out.println("its routes are: ");
            flyUS.showEdges(i);
        }
        */
        
        printGraph(flyUS.getEdgeGraph());
        
        
        // INSERT Min Spanning Tree Algorithm
        int[] verticesIncluded = new int[numberOfVertices];
        int numVerticesIncluded = 0;
        int[][] tempCopy = new int[numberOfVertices][numberOfVertices];
        int[][] mst = new int[numberOfVertices][numberOfVertices];
        int noEdge = 99; // Really high value so it will never be selected
        int rowMin,colMin,weightMin;
        int[] minHolder = new int[3];
        System.arraycopy(flyUS.getEdgeGraph(), 0, tempCopy, 0, numberOfVertices);
        
        verticesIncluded[0] = 0;
        numVerticesIncluded = 1;
        
        for(int i = 0; i < numberOfVertices; i++) {
            tempCopy[i][0] = noEdge;
        }
        while(numVerticesIncluded < numberOfVertices) {
            minHolder = findMinWeightEdge(tempCopy);
            rowMin = minHolder[0];
            colMin = minHolder[1];
            weightMin = minHolder[2];
            for(int i = 0; i < numberOfVertices; i++) {
                tempCopy[i][colMin] = noEdge;
            }
            mst[rowMin][colMin] = weightMin;
            mst[colMin][rowMin] = weightMin;
            verticesIncluded[numVerticesIncluded] = colMin;
            numVerticesIncluded++;
            
        }
        printGraph(mst);
        
    }
    
    public static int[] findMinWeightEdge(int[][] tempCopy) {
        
        printGraph(tempCopy);
        
        int rowMin = 0;
        int colMin = 0;
        int weightMin = 99;
        
        for(int x=0; x < tempCopy.length;x++) {
            for(int y=0; y < tempCopy[x].length;y++) {
                if(tempCopy[x][y] < weightMin) {
                    rowMin = x;
                    colMin = y;
                    weightMin = tempCopy[x][y];
                }
            }
        }
        
        
        int[] minHolder = new int[3];
        System.out.println(weightMin);
        minHolder[0] = rowMin;
        minHolder[1] = colMin;
        minHolder[2] = weightMin;
        return minHolder;
    }
    
    public static void printGraph(int[][] graph) {
        int output;
        for(int x=0;x < graph.length;x++){
            for(int y=0; y < graph[x].length;y++) {
                if(graph[x][y] == 99) {
                    output = 0;
                }else {
                    output = graph[x][y];
                }
                System.out.print(output + " ");
            }
            System.out.println();
        }
        System.out.println("--------------------------------------");
    }
}
