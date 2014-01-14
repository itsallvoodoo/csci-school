<?php
	include 'header.php';

	echo "<h1>Logs</h1>";

	session_start();
	$login = "";
	
	if(session_is_registered('myusername')){

		$sql = "SELECT * FROM joinLog_SensorEntry";
		$result = $mysqli->query($sql);

      	echo "<table border=1><tr><th>Creator</th><th>Type</th><th>data</th><th>Timestamp</th><th>Time Passed</th></tr>";

    	while($row = mysqli_fetch_array($result)) {
        	echo "<tr>";
        	echo "<td>".$row["entryCreator"]."</td>";
        	echo "<td>".$row["typeId"]."</td>";
        	echo "<td>".$row["data"]."</td>";
        	echo "<td>".$row["timestamp"]."</td>";
        	echo "<td></td>";
        	echo "</tr>";
		}

		echo "</table>";

		echo "<a href=add_record.php>Add Record</a><br>";
		echo "<a href=index.php>Home</a>";
	}
	else {
		echo "<a href=login.php>Log in</a>";
	}
?>
