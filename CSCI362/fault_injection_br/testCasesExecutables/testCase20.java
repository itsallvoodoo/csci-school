package testCasesExecutables;

import com.jpeterson.x10.beans.HouseCodeEditor;


public class testCase20 {

	public static void main(String[] args) {
	HouseCodeEditor editor = new HouseCodeEditor();
	
	editor.setValue('b');

	System.out.print(editor.getValue());	

	}


}
