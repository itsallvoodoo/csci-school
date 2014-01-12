package testCasesExecutables;

import com.jpeterson.util.BinaryFormat;



public class testCase03 {
    
	public static void main(String[] args) {

        BinaryFormat format = new BinaryFormat();
        
        System.out.print(format.format((long)0x4321fedc4321fedcL));
	}
}