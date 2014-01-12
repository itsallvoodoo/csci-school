/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package p13;

/**
 *
 * @author chadhobbs
 */
public class SimpleGraph // a directed graph
{

    Listing vertex[];  //the reference to the vertex array
    int edge[][];  // reference to the adjacency matrix array
    int max, numberOfVertices, highEdgeValue;

    public SimpleGraph(int n) {
        vertex = new Listing[n]; // allocation of the vertex array
        edge = new int[n][n];   // adjacency matrix with all elements set to 0
        max = n;
        numberOfVertices = 0;
        highEdgeValue = 99;
        for(int x=0; x < edge.length;x++) {
            for(int y=0; y < edge[x].length;y++) {
                    edge[x][y] = highEdgeValue;
            }
        }
    }

    public boolean insertVertex(int vertexNumber, Listing newListing) {
        if (vertexNumber >= max) {//the graph is full
            return false;
        }
        vertex[vertexNumber] = newListing.deepCopy();
        numberOfVertices++;
        return true;
    }

    public boolean insertEdge(int fromVertex, int toVertex, int weight) {
        if (vertex[fromVertex] == null || vertex[toVertex] == null) {// non-existent vertex
            return false;
        }
        edge[fromVertex][toVertex] = weight; // This is a weighted graph
        edge[toVertex][fromVertex] = weight; // Make it so it is a undirected graph
        return true;
    }

    public void showVertex(int vertexNumber) {
        System.out.println(vertex[vertexNumber]);
    }

    public void showEdges(int vertexNumber) {//edges emanating from vertexNumber

        for (int column = 0; column < numberOfVertices; column++) {
            if (edge[vertexNumber][column] > 0 &&edge[vertexNumber][column] < highEdgeValue) {// there is an edge

                System.out.println(vertexNumber + "," + column + " with weight: " + edge[vertexNumber][column]);
            }
        }
    }
    
    public int [][] getEdgeGraph() { return edge; }
}// end of SimpleGraph class

