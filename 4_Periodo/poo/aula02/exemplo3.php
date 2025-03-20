<?php
$xml = simplexml_load_file('paises.xml');

#exibe as informaçoes do objeto criado
foreach ($xml->children() as $elemento => $valor){
    echo "$elemento -> $valor <br>";
}