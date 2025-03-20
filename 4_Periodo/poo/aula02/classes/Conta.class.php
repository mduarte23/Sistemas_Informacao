<?php
abstract Class Conta {
    public $Agencia;
    public $Codigo;
    public $DataDeCriacao;
    public $Titular;
    public $Senha;
    public $Saldo;
    public $Cancelada;

    #criando um cronstrutor
    function __construct($agencia, $codigo, $dataDeCriacao, $titular, $senha, $saldo){
        $this->Agencia = $agencia;
        $this->Codigo = $codigo;
        $this->DataDeCriacao = $dataDeCriacao;
        $this->Titular = $titular;
        $this->Senha = $senha;

        #chama outro metodo da Classe
        $this->Depositar($saldo);
        $this->Cancelada = false;
    }

    #metodo retirar 
    #diminui o saldo da quantia
    function Retirar ($quantia){
        if ($quantia > 0){
            $this->Saldo -= $quantia;
        }
    }

    #metodo Depositar
    #aumenta o saldo da quantia
    function Depositar($quantia){
        if ($quantia > 0){
            $this->Saldo += $quantia;
        }
    }

    #metodo obterSaldo
    #mostra o saldo 
    function ObterSaldo(){
        return $this->Saldo;
    }

    abstract function Transferir($Conta, $Valor);

    #metodo destrutor
    #finaliza o objeto
    function __destruct(){
        echo "<br>
        Objeto Conta {$this->Codigo} de {$this->Titular->Nome} finalizada...
        <br>";
    }
}