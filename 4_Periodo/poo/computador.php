<?php

class Computador
{
    var $cpu;
    function ligar()
    {
        echo "Ligando computador  a {$this->cpu}... \n";  /*echo printa na tela*/ #\n pula linha
    }
}

$obj = new Computador;
$obj->cpu = "500Mhz"; 
$obj->ligar();

$novoobj = new Computador;
$novoobj->cpu = readline("Insira velocidade CPU: "); #readline = input 
$novoobj->ligar();