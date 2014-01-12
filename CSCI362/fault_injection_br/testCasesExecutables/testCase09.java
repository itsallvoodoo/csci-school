package testCasesExecutables;

import com.jpeterson.util.HexFormat;



public class testCase09 {
    
	public static void main(String[] args) {

        HexFormat format = new HexFormat();
        
        System.out.print(format.format((long)0x4321fedc4321fedcL));
	}
}
