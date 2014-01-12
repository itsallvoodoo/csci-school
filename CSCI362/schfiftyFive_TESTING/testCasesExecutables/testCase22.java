package testCasesExecutables;

import com.jpeterson.util.Condition;


public class testCase22 {

	public static void main(String[] args) {
	
		Condition var = new Condition(true);
		var.setFalse();
		System.out.print(var.isTrue());

	}


}
