<?php

class ContaCorrente extends Conta{
    public $Limite;

    #construtor
    #inicia a variavel limite
    function __construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo,$limite) {
         #Chamada de metodo construtor da classe pai
         parent::__construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo);
         $this->Limite = $limite;
    }

    function Retirar($quantia){
        if (($this->Saldo + $this->Limite) >= $quantia){
            #executa o metodo da classe pai
            parent::retirar($quantia);
        } else {
            echo "Retirada não Permitida...<br>";
            return false;
        }

    #retirada permitida
    return true;
    }
}