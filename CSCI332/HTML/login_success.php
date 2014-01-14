<?php
	session_start();
	if(session_is_registered(myusername)){
		header("location:modify_access_log.php");
	}
	else {
		header("location:login.php");
	}
?>
