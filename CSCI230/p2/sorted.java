package p2;

import java.lang.Math;

/**
 * This program contains the classes that insert, sort, fetch, and delete
 * entries into the database. Top and bottom behavior did not work according
 * to the code out of the book and custom handling procedures had to be written
 * for the first entry, second entry, and then any entry that was either at
 * the top of the list or bottom of the list. There has to be a better way.
 * 
 * @author chadhobbs
 */
public class sorted {

    private int next;
    private Node[] data;
    private int size;

    public sorted() {
        next = 0;
        size = 100;
        data = new studentListings[5];
    }

    public sorted(int s) {
        next = 0;
        size = s;
        data = new studentListings[s];
    }

    public boolean insert(Node newListing) {
        if (next == 0) {
            data[next] = newListing;
            next++;
            return true;
        }
        if (next == 1) {
            if (newListing.getKey().compareTo(data[0].getKey()) > 0) {
                data[1] = newListing;
            } else {
                data[1] = data[0].deepCopy();
                data[0] = newListing;
            }
            next++;
            return true;
        }
        // Second attempt

        int low = 0;
        int high = next - 1;
        int i = (low + high) / 2;
        if (i < 0) {
            i = 0;
        }
        while (true) {
            if (low <= 0 && high <= 0 && newListing.getKey().compareTo(data[0].getKey()) < 0) {
                i = 0;
                System.out.print(newListing.getKey());
                System.out.println(" went to bottom of stack");
                break;
            } else if (newListing.getKey().compareTo(data[next - 1].getKey()) > 0) {
                i = next;
                System.out.print(newListing.getKey());
                System.out.println(" went to top of stack");
                break;
            } else if ((high - low) <= 1
                    && newListing.getKey().compareTo(data[i].getKey()) > 0
                    && newListing.getKey().compareTo(data[i + 1].getKey()) < 0) {
                i = i + 1;
                System.out.print(newListing.getKey());
                System.out.println(" went to middle of stack");
                break;
            } else if (newListing.getKey().compareTo(data[i].getKey()) < 0) {
                high = i - 1;
                i = (high + low) / 2;
            } else {
                low = i + 1;
                i = (high + low) / 2;
            }

        }

        for (int j = next; j > i; j--) {
            data[j] = data[j - 1];
        }
        next++;
        data[i] = newListing.deepCopy();
        showAll();
        return true;
    }

    public Node fetch(String targetKey) {
        int low = 0;
        int high = next - 1;
        int i = (low + high) / 2;
        while (targetKey.compareTo(data[i].getKey()) != 0) {
            if (targetKey.compareTo(data[i].getKey()) < 0 && high != low) {
                high = i - 1;
            } else {
                low = i + 1;
            }
            i = (low + high) / 2;
        }
        return data[i].deepCopy();
    }

    public boolean delete(studentListings targetKey) {
        int low = 0;
        int high = next - 1;
        int i = (low + high) / 2;
        while (targetKey.getKey().compareTo(data[i].getKey()) != 0 && high != low) {
            if (targetKey.getKey().compareTo(data[i].getKey()) < 0) {
                high = i - 1;
            } else {
                low = i + 1;
            }
            i = (low + high) / 2;
        }
        for (int j = i; j < next - 1; j++) {
            data[j] = data[j + 1];
        }
        next = next - 1;
        data[next] = null;

        return true;
    }

    public boolean update(studentListings targetKey, studentListings newNode) {
        if (delete(targetKey) == false) {
            return false;
        } else if (insert(newNode) == false) {
            return false;
        } else {
            return true;
        }
    }// end of update method

    public void showAll() {
        for (int i = 0; i < next; i++) {
            System.out.println(data[i].toString());
        }
    }
}
