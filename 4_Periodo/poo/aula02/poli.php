<?php

include_once 'classes/Pessoa.class.php';
include_once 'classes/Conta.class.php';
include_once 'classes/ContaPoupanca.php';
include_once 'classes/ContaCorrente.php';

$carlos = new Pessoa(10, "Carlos da Silva", 185, 25, "10/04/1976", "Ensino Medio", 650.00);
#var_dump($carlos);

echo "Manipulando o objeto {$carlos->Nome}: <br>";
#criando um array
$contas[1] = new ContaCorrente(6777, "CC.12345-6", "10/07*02", $carlos, 9876, 500.00, 200.00);
$contas[2] = new ContaPoupanca(6778, "PP.12345-7", "10/07/02", $carlos, 9876, 500.00, "10/07");
#var_dump($contas);
#Percorrendo as contas
foreach ($contas as $key => $conta) {
    echo "<br>Manipulando a conta $key de {$conta->Titular->Nome}: <br>";
    echo "O saldo atual da conta $key é r\$ {$conta->ObterSaldo()} <br>";
    $conta->Depositar(200);
    echo "O saldo atual da conta $key é R\${$conta->ObterSaldo()} <br>";
    $conta->Retirar(100);
    echo "O saldo atual da conta $key é R\$ {$conta->ObterSaldo()} <br>";
}