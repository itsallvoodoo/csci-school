package p4;

/**
 *
 * @author chadhobbs
 */
public class SingleLinkList {

    private Node h;

    public SingleLinkList() {
        h = new Node();
        h.setL(null);
        h.setNext(null);

    }
    
    public boolean insert(Listing newListing) {
        Node n = new Node();
        
        if(n == null) {
            return false;
        }
        else {
            n.setNext(h.getNext());
            h.setNext(n);
            n.setL(newListing.deepCopy());
            return true;
        }
    }
    
    public Listing fetch(String targetKey) {
        Node p = h.getNext();
        
        while(p != null && !(p.getL().compareTo(targetKey) == 0)) {
            p = p.getNext();
        }
        if(p != null) {
            return p.getL().deepCopy();
        }
        else {
            return null;
        }
    }
    
    public Listing getLast() {
        Node p = h.getNext();
        
        while(p.getNext() != null) {
            p = p.getNext();
        }
        if(p != null) {
            return p.getL().deepCopy();
        }
        else {
            return null;
        }
    }
    
    public boolean delete(String targetKey) {
        Node q = h;
        Node p = h.getNext();
        
        while(p != null && !(p.getL().compareTo(targetKey) == 0)) {
            q = p;
            p = p.getNext();
        }
        if (p != null) {
            q.setNext(p.getNext());
            return true;
        }
        else {
            return false;
        }
    }
    
    public boolean update(String targetKey, Listing newListing) {
        if (delete(targetKey) == false) {
            return false;
        }
        else if (insert(newListing) == false) {
            return false;
        }
        return false;
    }
    
    public void showAll() {
        Node p = h.getNext();
        while (p != null) {
            System.out.println(p.getL().toString());
            p = p.getNext();
        }
    }
}
