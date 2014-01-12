package ACMCodeComp;

import java.util.Scanner;

/**
 *
 * @author chadhobbs
 */
public class problemG {

    public static void main(String[] args) {

        int a;

        Scanner in = new Scanner(System.in);
        String[] storage = new String[40];


        for (int i = 0; i < 20; i++) {
            storage[i] = in.nextLine();
            storage[i + 10] = in.nextLine();

            if ((storage[i] == null ? storage[i + 10] == null : storage[i].equals(storage[i + 10])) && "E".equals(storage[i])) {
                break;
            }
        }


        for (int i = 0; i < 20; i++) {
            if (storage[i].charAt(0) == 'E') {
                break;
            }

            int p1 = 0;
            int p2 = 0;
            for (int j = 0; j < storage[i].length(); j++) {
                if (storage[i].charAt(j) == 'R' && storage[i + 10].charAt(j) == 'S') {
                    p1 = p1 + 1;
                }
                if (storage[i].charAt(j) == 'P' && storage[i + 10].charAt(j) == 'R') {
                    p1 = p1 + 1;
                }
                if (storage[i].charAt(j) == 'S' && storage[i + 10].charAt(j) == 'P') {
                    p1 = p1 + 1;
                }
                if (storage[i].charAt(j) == 'S' && storage[i + 10].charAt(j) == 'R') {
                    p2 = p2 + 1;
                }
                if (storage[i].charAt(j) == 'R' && storage[i + 10].charAt(j) == 'P') {
                    p2 = p2 + 1;
                }
                if (storage[i].charAt(j) == 'P' && storage[i + 10].charAt(j) == 'S') {
                    p2 = p2 + 1;
                }

            }
            System.out.print("P1: ");
            System.out.println(p1);
            System.out.print("P2: ");
            System.out.println(p2);

        }
    }
}
