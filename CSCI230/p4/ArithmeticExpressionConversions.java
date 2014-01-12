/**
 * ArithmeticExpressionConversions.java
 * 
 * CSCI 230
 * Fall 2012
 * Chad Hobbs
 * Due: 11SEP12
 * 
 * 
 * ArithmeticExpressionConversions provides methods for the driver class and
 * executes the Stack class to manage stacks.
 */
package p4;

/**
 * @author chadhobbs
 */
public class ArithmeticExpressionConversions {

    /**
     * input stores the re-formatted user input, stored as a string to handle any character
     */
    private String[] input;
    /**
     * Creates a stack used to convert infixed notation to postfixed
     */
    private SingleLinkList postStack;
    /**
     * Holds postfixed entries
     */
    private String[] postString;

    /**
     * Default Constructor
     */
    public ArithmeticExpressionConversions() {

        this(50);

    }

    /**
     * Full Constructor
     * @param input
     * @param postStack
     * @param postString
     * 
     */
    public ArithmeticExpressionConversions(int s) {

        input = new String[s];
        postStack = new SingleLinkList();
        postString = new String[s];

    }

    /**
     * Converts an infixed string array to a postfixed string array
     * @return 
     */
    public boolean convertInfixToPostfix() {

        int i = 0;
        int j = 0;
        while (input[i] != null) {

            if (input[i].compareTo("+") == 0
                    || input[i].compareTo("-") == 0
                    || input[i].compareTo("*") == 0
                    || input[i].compareTo("/") == 0
                    || input[i].compareTo("(") == 0) {
                
                postStack.insert(new Listing(input[i]));
                
            } else if (input[i].compareTo(")") == 0) {
                boolean repeat = true;
                String comp = postStack.getLast().getListing();
                while (comp != null) {
                    if(comp.compareTo("(") != 0) {
                        break;
                    }
                    postString[j] = postStack.getLast().getListing();
                    postStack.delete(postStack.getLast().getListing());
                    comp = postStack.getLast().getListing();
                    j++;
                }
                postString[j] = postStack.getLast().getListing();
                    postStack.delete(postStack.getLast().getListing());
            } else {
                postString[j] = input[i];
                j++;

            }
            i++;
        }
        String holder;
        while (postStack.getLast() != null) {
            holder = postStack.getLast().getListing();
            postStack.delete(postStack.getLast().getListing());
            if (holder.compareTo("(") != 0) {
                postString[j] = holder;
                j++;
            }
        }
        return true;
    }

    public int getValue(String s) {
        if (s.compareTo("+") == 0) { return 1; }
        if (s.compareTo("-") == 0) { return 1; }
        if (s.compareTo("/") == 0) { return 2; }
        if (s.compareTo("*") == 0) { return 2; }
        else { return 3; }
    }

    /**
     * Calculates the value of a postfixed string array
     * @return 
     */
    public int evaluatePostfixExpression() {
        int value1;
        int value2;
        SingleLinkList evalStack = new SingleLinkList();
        int i = 0;

        while (postString[i] != null) {
            if (postString[i].compareTo("+") == 0) {
                value1 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                value2 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                evalStack.insert(new Listing(Integer.toString(value2 + value1)));
            } else if (postString[i].compareTo("-") == 0) {
                value1 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                value2 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                evalStack.insert(new Listing(Integer.toString(value2 - value1)));
            } else if (postString[i].compareTo("*") == 0) {
                value1 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                value2 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                evalStack.insert(new Listing(Integer.toString(value2 * value1)));
            } else if (postString[i].compareTo("/") == 0) {
                value1 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                value2 = Integer.parseInt(evalStack.getLast().getListing());
                evalStack.delete(postStack.getLast().getListing());
                evalStack.insert(new Listing(Integer.toString(value2 / value1)));
            } else {
                evalStack.insert(new Listing(postString[i]));
            }
            i++;
        }
        return Integer.parseInt((evalStack.getLast().getListing()));
    }

    /**
     * Takes user input and either formats it or informs user of first found error
     * @param n
     * @return 
     */
    public boolean processEntry(String n) {
        String[] test = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "(", ")"};
        int balance = 0;
        int index = 0;
        boolean intFlag = false;
        for (int i = 0; i < n.length(); i++) {

            for (int j = 0; j <= test.length; j++) {

                if (j > 10) {
                    intFlag = false;
                }
                if (n.substring(i, i + 1).compareTo(" ") == 0) {
                    break;
                }
                if (j >= 17) {
                    System.out.print("Entry validity check: False - improper character: '");
                    System.out.println(n.charAt(i) + "'");
                    return false;
                }
                if (n.substring(i, i + 1).compareTo(test[j]) == 0) {
                    if (j == 15) {
                        balance++;
                    }
                    if (j == 16) {
                        balance--;
                    }
                    if (intFlag) {
                        input[index - 1] = input[index - 1] + test[j];
                    } else {
                        input[index] = test[j];
                        index++;
                        if (j < 11) {intFlag = true;}
                    }
                    break;
                }
            }
        }
        if (balance == 0) {
            System.out.println("Entry validity check: True");
            return true;
        } else {
            System.out.println("Entry validity check: False - Parenthesis unbalanced");
            return false;
        }
    }

    /**
     * Provides a method to compare strings to one another
     * @param targetKey
     * @return 
     */
    public int compareTo(Object targetKey) {
        String tKey = (String) targetKey;
        return (this.compareTo(tKey));
    }

    /**
     * Displays what the user entered but reformatted
     */
    public void printInput() {
        for (int i = 0; i < input.length; i++) {
            if (input[i] != null) {
                System.out.print(input[i]);
            }
        }
        System.out.println();

    }

    public boolean matchTest(String s) {
        String[] test = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"};
        
        for(int i = 0;i < test.length;i++) {
            if(s.compareTo(test[i]) == 0) {
                return true;
            }
        }
        return false;
    }
    
    
    /**
     * Displays postfixed string array
     */
    public void printPostString() {

        int i = 0;
        while (postString[i] != null) {
            System.out.print(postString[i] + " ");
            i++;
        }
        System.out.println();
    }

    /**
     * Sets a value in the entry array
     * @param n
     * @param i 
     */
    public void setEntry(String n, int i) {
        input[i] = n;
    }

    /**
     * Retrieves an entry in the entry array
     * @param i
     * @return 
     */
    public String getEntry(int i) {
        return input[i];
    }
}
