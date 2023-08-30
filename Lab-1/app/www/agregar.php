<?php

$conn = mysqli_connect('db', 'root', 'test', "dbname");

$nombre = $_POST['nombre'];

$query = "INSERT INTO Person(id, name) VALUES (5, '$nombre')";

$result = mysqli_query($conn, $query);

mysqli_close($conn);

?>