package testCasesExecutables;

import com.jpeterson.util.HexFormat;



public class testCase07 {
    
	public static void main(String[] args) {

        HexFormat format = new HexFormat();
        
        System.out.print(format.format((short)0xa2b6));
	}
}
