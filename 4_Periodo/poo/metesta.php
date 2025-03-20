<?php
class Aplicacao {
    /*metodo estatico
    lê o arquivo readme.txt
    */
    static function Sobre(){
        $fd = fopen('readme.txt', 'r');
        while ($linha = fgets($fd   )){
            echo $linha;
        }
    }
}

echo "Informações sobre a aplicação: <br>";
echo "===============================<br>";
Aplicacao::Sobre();