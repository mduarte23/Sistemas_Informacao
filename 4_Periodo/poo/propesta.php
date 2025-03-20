<?php
class Aplicacao{
    static $Quantidade;
    #Metodo Construtor
    #incrementa a $Quantidade de Aplicacoes
    function __construct($Nome){
        //incrementa propriedade estática
        self::$Quantidade++;
        $i = self::$Quantidade;
        echo "Nova aplicação nr. $i: $Nome<br>";
    }
}

#cria novos objetos
new Aplicacao('Dia');
new Aplicacao('Gimp');
new Aplicacao('Gnumeric');
new Aplicacao('Abiword');
new Aplicacao('Evolution');
echo 'Quantidade de Aplicações = ' . Aplicacao::$Quantidade. '<br>';