<?php 
include( 'php/conexion.php' );
if( isset( $_POST['nombres'] ) ){
    foreach( $_POST['nombres'] as $indice => $nombre ){
        $apellido = $_POST['apellidos'][$indice];
        $consulta_sql = "INSERT INTO usuarios SET nombre='$nombre', apellido='$apellido'";

        mysqli_query( $cnx, $consulta_sql );        
    }
}
header("Location: index.php" );