<?php
	session_start();
    include 'header.php';
  	$user = $_REQUEST["id"];

	$id = 0;
	$fname = "";
	$lname = "";
	$level = "";
	$login = "";
	$code = "";


  	if(isset($_POST['update'])) {

  		$id = $_POST['idUsers'];
		$fname = $_POST['f_name'];
		$lname = $_POST['l_name'];
		$level = $_POST['access'];
		$login = $_POST['login'];
		$code = $_POST['code'];

		if($id == 0){
			$sql = 	"INSERT INTO Users ".
					"SET idUsers=DEFAULT, fName='$fname', lName='$lname', accessLevel='$level', loginName='$login', accessCode='$code' ";

		}
		else {
	        $sql = 	"UPDATE Users".
	        		" SET fName='$fname', lName='$lname', accessLevel='$level', loginName='$login', accessCode='$code' ".
	        		"WHERE idUsers='$id'";
        }
		$result = $mysqli->query($sql);
		if(!$result) {
  			die('Could not update data: ' . $mysqli->error);
  			echo "<a href=index.php>Home</a>";
		}
		else {
			header("location:index.php");
		}
    }
  	else {

  		if($user != 0){
		  	$sql = "SELECT * FROM Users WHERE idUsers='$user' LIMIT 0,1";
			$result = $mysqli->query($sql);
			$row = $result->fetch_array();

			$id = $row[idUsers];
			$fname = $row[fName];
			$lname = $row[lName];
			$level = $row[accessLevel];
			$login = $row[loginName];
			$code = $row[accessCode];
		}

		echo '<h1>Update User</h1>';
		echo '<table border=1>';
		echo '<form action="" method="post" action="'.$_PHP_SELF.'">';
		echo '<input type="hidden" name="idUsers" value="'.$id.'">';
		echo '<tr><td>First Name: </td><td><input type="text" name="f_name" value="'.$fname.'" required></td</tr>';
		echo '<tr><td>Last Name: </td><td><input type="text" name="l_name" value="'.$lname.'" required></td</tr>';
		echo '<tr><td>Access Level: </td><td><input type="text" name="access" value="'.$level.'" required></td</tr>';
		echo '<tr><td>User Name: </td><td><input type="text" name="login" value="'.$login.'" required></td</tr>';
		echo '<tr><td>Password: </td><td><input type="text" name="code" value="'.$code.'" required></td</tr>';
		echo '<tr><td><input type="submit" name="update" value="Submit"></td><td>';
		echo '<input type="button" value="Go Back" onclick="go_home();"></td></tr>';
		echo '</form>';
		echo '</table>';

	}
?>

<script>
	function go_home() {
  		window.location = 'index.php';
	}
</script>