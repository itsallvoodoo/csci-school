<?php

	session_start();
	$last_user = $_SESSION['myusername'];
	session_destroy();
	header("location:modify_access_log.php?last_user=$last_user");
?>