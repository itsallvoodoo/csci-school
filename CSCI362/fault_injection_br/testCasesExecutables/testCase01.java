package testCasesExecutables;

import com.jpeterson.util.BinaryFormat;



public class testCase01 {
    
	public static void main(String[] args) {

        BinaryFormat format = new BinaryFormat();
        format.setDivider(" ");
        
        System.out.print(format.format((byte)0x04));
	}
}
