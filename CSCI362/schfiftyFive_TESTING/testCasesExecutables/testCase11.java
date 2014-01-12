package testCasesExecutables;

import org.openremote.controller.utils.PathUtil;

public class testCase11 {

	public String testPathUtil() {
		String test_dir = "testing/subdir/subdir2";
		return PathUtil.addSlashSuffix(test_dir);
	}

	public static void main(String[] args) {
		testCase11 test = new testCase11();
		System.out.print(test.testPathUtil());
	}
}