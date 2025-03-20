<?php

$frutas = ['abacate', 'banana', 'pera', 'maça'];

#echo $frutas[2];
#echo $frutas[0];

foreach ($frutas as $id => $valor){
    echo $id . '-'.  $valor . '<br>';
}