<?php
Class Pessoa{
    public $Codigo;
    public $Nome;
    public $Altura;
    public $Idade;
    public $Nascimento;
    public $Escolaridade;
    public $Salario;

    #criando um costrutor
    function __construct($codigo, $nome, $altura, $idade, $nascimento, $escolaridade, $salario){
        $this->Codigo = $codigo;
        $this->Nome = $nome;
        $this->Altura = $altura;
        $this->Idade = $idade;
        $this->Nascimento = $nascimento;
        $this->Escolaridade = $escolaridade;
        $this->Salario = $salario;

    }

    #metodo para Crescer
    #aumenta  a altura em centimetros
    function Crescer($centimetros){
        if ($centimetros>0){
            $this->Altura += $centimetros;
        }   
    }

    # metodo para formar
    #altera a escolaridade

    function Formar($titulacao){
        $this->Escolaridade = $titulacao;
    }

    #metodo envelhecer
    #aumenta a idade em anos
    function Envelhecer($anos){
        if ($anos > 0){
            $this->Idade += $anos;
        }
    }

    #metodo destrutor
    #finaliza o objeto
    function __destruct(){
        echo "Objeto {$this->Nome} finalizando...<br>";
    }
}