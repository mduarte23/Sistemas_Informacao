<?php

include 'classes/Funcionario.class.php';
include 'classes/Estagiario.class.php';

$pedrinho = new Estagiario;
$pedrinho->SetSalario(248);

echo "O salário do Pedrinho é R$: ".$pedrinho->GetSalario()."<br>";