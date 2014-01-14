<?php
	include 'header.php';

	echo "<h1>Welcome to the Home Security System Main Page</h1>";

	session_start();
	$login = "";
	
	if(session_is_registered('myusername')){
		$login = $_SESSION['myusername'];

		$sql = "SELECT * FROM Users WHERE loginName='$login' LIMIT 0,1";
		$result = $mysqli->query($sql);
		$row = $result->fetch_array();

			if(strlen($row[fName]) > 0) {

				echo "Hello " . $row[fName] . "<br>";
				echo "<a href=view_logs.php>View Logs</a><br>";
				echo "<a href=modify_user.php?id=".$row[idUsers].">Edit Account</a><br>";

				if($row[accessLevel] == 1) {
					echo "<a href=list_users.php>Manage Users</a><br>";
				}

				echo "<a href=logout.php>Log out</a>";
			}
			else {
				echo "No user found, please log in";
				echo "<a href=login.php>Log in</a>";
			}
	}
	else {
		echo "<a href=login.php>Log in</a>";
	}
?>
