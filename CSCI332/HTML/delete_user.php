<?php
	session_start();
    include 'header.php';
  	$user = $_REQUEST["id"];

  	$sql = 	"DELETE FROM Users WHERE idUsers='$user'";
	$result = $mysqli->query($sql);
	header("location:list_users.php");
 ?>