package testCasesExecutables;

import java.util.Hashtable;
import java.net.Socket;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.io.IOException;

import com.jpeterson.pool.SocketObjectPool;

public class testCase14 {

	public String testSocketObjectPoolCheckOut() {
		try {
			int port = 9090;
			ServerSocket s_sock = new ServerSocket(port);
			SocketObjectPool pool = new SocketObjectPool(InetAddress.getLocalHost(), port);
			Socket s = (Socket) pool.borrowObject();

			if (s == null)
				return "Null";
			pool.returnObject(s);
			return Boolean.toString(pool.isSocketCheckedIn(s));

		} catch (IOException e) {
			return e.toString();
		}
	}

	public static void main(String[] args) {
		testCase14 test = new testCase14();
		System.out.print(test.testSocketObjectPoolCheckOut());
	}
}