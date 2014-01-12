package testCasesExecutables;

import org.openremote.controller.utils.PathUtil;

public class testCase12 {

	public String testPathUtil() {
		String test_dir = "testing/subdir/subdir2/";
		return PathUtil.removeSlashSuffix(test_dir);	
	}

	public static void main(String[] args) {
		testCase12 test = new testCase12();
		System.out.print(test.testPathUtil());
	}
}