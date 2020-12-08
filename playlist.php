<?php
if(isset($_POST['envoi']))    //if form submitted
{ 

$arg = htmlspecialchars($_POST["lumi"]);  //get the first parameter
$arg2 = htmlspecialchars($_POST["temp"]);   //get the second parameter
exec("python playlist.py $arg $arg2");  //runs the playlist.py program

}
?>
