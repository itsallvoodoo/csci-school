package testCasesExecutables;

import org.openremote.controller.statuscache.ChangedStatusRecord;

public class testCase25 {

	public static void main(String[] args) {
	
		Integer[] array = {1, 2, 3, 4, 5};
		ChangedStatusRecord csr = new ChangedStatusRecord("Device", array);
		
		csr.setDeviceID("DifferentDevice");
		
		System.out.print(csr.getDeviceID());
	
	}

}