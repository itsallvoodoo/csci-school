package testCasesExecutables;

import java.util.Hashtable;
import java.net.Socket;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.io.IOException;

import com.jpeterson.pool.SocketObjectPool;

public class testCase15 {

	public String testSocketObjectPoolCheckOut() {
		try {
			int port = 9090;
			ServerSocket s_sock = new ServerSocket(port);
			SocketObjectPool pool = new SocketObjectPool(InetAddress.getLocalHost(), port);
			Socket s = (Socket) pool.borrowObject();

			if (s == null)
				return "Null";
			pool.returnBrokenObject(s);
			return Boolean.toString(pool.isSocketCheckedIn(s)) + "\n" +
				Boolean.toString(pool.isSocketCheckedOut(s));

		} catch (IOException e) {
			return e.toString();
		}
	}

	public static void main(String[] args) {
		testCase15 test = new testCase15();
		System.out.print(test.testSocketObjectPoolCheckOut());
	}
}