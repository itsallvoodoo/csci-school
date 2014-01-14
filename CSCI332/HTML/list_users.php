<?php
	session_start();
    include 'header.php';
  	$login = $_SESSION['myusername'];

  	$sql = "SELECT accessLevel FROM Users WHERE loginName='$login' LIMIT 0,1";
	$result = $mysqli->query($sql);
	$row = $result->fetch_array();

	if($row["accessLevel"] == 1) {
?>
    <table border=1>
      <tr><th>First Name</th><th>Last Name</th><th>User Name</th><th>Access Level</th><th>Password</th><th>Action</th><th>Delete?</th></tr>
      <?php

    		$sql = "SELECT * FROM Users";

        $result = $mysqli->query($sql);

          while($row = mysqli_fetch_array($result)) {
            echo "<tr>";
            echo "<td>".$row["fName"]."</td>";
            echo "<td>".$row["lName"]."</td>";
            echo "<td>".$row["loginName"]."</td>";
            echo "<td>".$row["accessLevel"]."</td>";
            echo "<td>".$row["accessCode"]."</td>";
            echo "<td><a href=modify_user.php?id=".$row["idUsers"].">Edit</a></td>";
            echo "<td><a href=delete_user.php?id=".$row["idUsers"].">Delete User</a></td>";
            echo "</tr>";
          }
      ?>
    </table>
    <a href=modify_user.php?id=0>Add User</a><br>
    <a href=index.php>Home</a>

<?php
	}
	else {
		echo "<center><h1>Permission Denied<h1></center><br>";
		echo "<a href=index.php>Home</a>";
	}
?>