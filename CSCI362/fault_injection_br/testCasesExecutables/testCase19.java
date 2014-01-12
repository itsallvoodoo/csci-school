package testCasesExecutables;

import com.jpeterson.x10.X10Util;


public class testCase19 {

	public static void main(String[] args) {
	X10Util util = new X10Util();
      
 	byte nibble = (byte)1;

	System.out.print(util.byte2houseCode(nibble));	

	}


}
