<?php
	include 'header.php';

	$myusername=$_POST['myusername'];
	$mypassword=$_POST['mypassword'];

	// ATTEMPT AT INPUT VALIDATION
	//$myusername = stripslashes($myusername);
	//$mypassword = stripslashes($mypassword);
	//$myusername = mysql_real_escape_string($myusername);
	//$mypassword = mysql_real_escape_string($mypassword);

	$sql="SELECT * FROM Users WHERE loginName='$myusername' and accessCode='$mypassword'";
	$result = $mysqli->query($sql);



	$count=$result->num_rows;

	if($count==1){

		session_register("myusername");
		session_register("mypassword");
		header("location:login_success.php");
	}
	else {

?>
		<center>Wrong Username or Password</center><br>
		<center><a href=login.php>Log In</a>&nbsp; &nbsp; &nbsp; <a href=index.php>Home</a></center>
<?php
	}

	ob_end_flush();
?>