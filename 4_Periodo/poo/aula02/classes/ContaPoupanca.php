<?php

 final class ContaPoupanca extends Conta{
    public $Aniversario;

    #construtor
    #inicia a variavel limite
    function __construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo,$aniversario) {
         #Chamada de metodo construtor da classe pai
         parent::__construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo);
         $this->Aniversario = $aniversario;
    }
    function Transferir($Conta, $Valor){
        if ($this->Retirar($Valor)){
            $Conta->Depositar($Valor);
        }
    }
    function Retirar($quantia){
        if ($this->Saldo  >= $quantia){
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