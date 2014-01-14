<?php
	include 'header.php';
	session_start();
	if(session_is_registered('myusername')){
		
		if(isset($_POST['update'])) {
			$user = $_POST['user'];
			$type = $_POST['sensortype'];
			$data = $_POST['sensordata'];

			$sql = 	"INSERT INTO SensorEntry ".
					"SET idSensorEntry=DEFAULT, typeId='$type', userTriggered='$user', data='$data'";
			$result = $mysqli->query($sql);

			header("location:view_logs.php");
		}
		else {

			$login = $_SESSION['myusername'];

			$sql = "SELECT idUsers FROM Users WHERE loginName='$login' LIMIT 0,1";
			$result = $mysqli->query($sql);
			$row = $result->fetch_array();

			echo '<table width="300" border="0" align="center" cellpadding="0" cellspacing="1" bgcolor="#CCCCCC">';
			  echo '<tr>';
			    echo '<form name="form1" method="post" action="'.$_PHP_SELF.'">';
			    	echo '<input name="user" type="hidden" value="'.$row[idUsers].'">';
			      echo '<td>';
			        echo '<table width="100%" border="0" cellpadding="3" cellspacing="1" bgcolor="#FFFFFF">';
			          echo '<tr>';
			            echo '<td colspan="3"><strong>Add Record</strong></td>';
			          echo '</tr>';
			          echo '<tr>';
			            echo '<td width="78">Record Type</td>';
			            echo '<td width="6">:</td>';
			            echo '<td width="294">';
			            	echo '<select name="sensortype">';
								echo '<option value="1">Camera</option>';
								echo '<option value="2">Motion</option>';
								echo '<option value="3">Door</option>';
							echo '</select></td>';
			          echo '</tr>';
			          echo '<tr>';
			            echo '<td>Sensor Data</td>';
			            echo '<td>:</td>';
			            echo '<td><input name="sensordata" type="text"></td>';
			          echo '</tr>';
			          echo '<tr>';
			            echo '<td>&nbsp;</td>';
			            echo '<td>&nbsp;</td>';
			            echo '<td><input type="submit" name="update" value="Submit"></td>';
			          echo '</tr>';
			        echo '</table>';
			      echo '</td>';
			    echo '</form>';
			  echo '</tr>';
			echo '</table>';
		}
	}
	else {
		header("location:index.php");

	}
?>


