package testCasesExecutables;

import com.jpeterson.pool.SocketObjectPool;
import java.net.Socket;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.io.IOException;

public class testCase13 {

	public String testSocketObjectPoolCheckOut() {
		try {
			int port = 9090;
			ServerSocket s_sock = new ServerSocket(port);
			SocketObjectPool pool = new SocketObjectPool(InetAddress.getLocalHost(), port);
			Socket s = (Socket) pool.borrowObject();
			if (s == null)
				return "Null";
			String port_str = Integer.toString(s.getPort());
			s.close();
			s_sock.close();
			return port_str;
		} catch (IOException e) {
			return e.toString();
		}
	}

	public static void main(String[] args) {
		testCase13 test = new testCase13();
		System.out.print(test.testSocketObjectPoolCheckOut());
	}
}