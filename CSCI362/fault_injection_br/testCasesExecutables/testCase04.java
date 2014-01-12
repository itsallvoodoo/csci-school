package testCasesExecutables;

import com.jpeterson.util.BinaryFormat;



public class testCase04 {
    
	public static void main(String[] args) {

        BinaryFormat format = new BinaryFormat();
        
        System.out.print(format.format((int)0x4321fedc));
	}
}