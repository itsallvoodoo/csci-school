package testCasesExecutables;

import com.jpeterson.util.HexFormat;



public class testCase08 {
    
	public static void main(String[] args) {

        HexFormat format = new HexFormat();
        
        System.out.print(format.format((int)0x4321fedc));
	}
}
