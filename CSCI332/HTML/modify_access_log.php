<?php
	include 'header.php';

	session_start();

	$refurl = parse_url($_SERVER['HTTP_REFERER']);
	$login = $_SESSION['myusername'];
	$source = $refurl[path];
	


	if($source == "/login.php") {

		$sql = "SELECT idUsers FROM Users WHERE loginName='$login' LIMIT 0,1";
		$result = $mysqli->query($sql);
		$row = $result->fetch_array();
		$user_id = $row[idUsers];

		$sql = "INSERT INTO accessLog  (Users_idUsers, timestamp, login)
			VALUES ($user_id,now(),1)";
		
	}
	else {

		$id = $_REQUEST["last_user"];
		echo $id;
		$sql = "SELECT idUsers FROM Users WHERE loginName='$id' LIMIT 0,1";
		$result = $mysqli->query($sql);
		$row = $result->fetch_array();
		$user_id = $row[idUsers];

		$sql = "INSERT INTO accessLog  (Users_idUsers, timestamp, login)
			VALUES ($user_id,now(),0)";

	}

	$result = $mysqli->query($sql);
	header("location:index.php");

?>