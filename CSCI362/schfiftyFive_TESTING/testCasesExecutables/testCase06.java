package testCasesExecutables;

import com.jpeterson.util.HexFormat;



public class testCase06 {
    
	public static void main(String[] args) {

        HexFormat format = new HexFormat();
        
        System.out.print(format.format((byte)0x33));
	}
}
