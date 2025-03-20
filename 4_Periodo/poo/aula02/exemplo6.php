<?php
$xml = simplexml_load_file('paises2.xml');

#altera as propriedades
$xml->populacao = '220 milhões';
$xml->religiao = 'cristianismo';
$xml->geografia->clima = 'Temperado';
$xml->addChild('presidente', 'Chapolin Colordo');

#exibindo o novo XML
echo $xml->asXML();
#grava no arquivo paises.xml
file_put_contents('paises2.xml', $xml->asXML());