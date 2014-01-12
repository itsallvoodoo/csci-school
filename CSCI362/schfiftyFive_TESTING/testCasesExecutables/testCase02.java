package testCasesExecutables;

import com.jpeterson.util.BinaryFormat;



public class testCase02 {
    
	public static void main(String[] args) {

        BinaryFormat format = new BinaryFormat();
        format.setDivider(" ");
        
        System.out.print(format.format((short)0xa2b6));
	}
}