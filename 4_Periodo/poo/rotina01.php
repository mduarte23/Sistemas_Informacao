<?php

#Captura valor variavel
$umidade = readline("Insira o valor da umidade: ");
#Testa se é maior que 90. Retorna um Boolean
$vai_chover = ($umidade>90);

#testa se $vai_chover é verdadeiro
if ($vai_chover){
    echo "Está chovendo";
}else{
    echo "Não vai chover";
}