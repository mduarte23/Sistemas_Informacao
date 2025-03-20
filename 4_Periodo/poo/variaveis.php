<?php

$carros = ["Gol","Variante","Pampa","Pegout 206"];

#exibe o array na posição [x]
#echo $carros[2];

var_dump($carros);
echo "<br>";

#percorre o array e salva o item em list
foreach($carros as $list){
    echo $list, "<br>";
}
echo "<br>";
#asort organiza por ordem alfabetica
asort($carros);
foreach($carros as $list){
    echo $list, "<br>";
}
#informa o que esta guardado dentro da variavel
var_dump($carros);

#print_r lista todos itens
#print_r($carros);

