<?php

$conn = mysqli_connect('db', 'root', 'test', "dbname");

$nombre = $_POST['nombre'];

$apellido = $_POST['apellido'];

$query = "INSERT INTO Person(id, name, last_name) VALUES (NULL, '$nombre', '$apellido')";

$result = mysqli_query($conn, $query);

mysqli_close($conn);

?>