<?php

//insere a classe da pasa classes 
include_once 'classes/Produto.class.php'; #import da pasta classes

$produto = new Produto; #cria um novo produto usando a class
$produto2 = new Produto; #cria um novo produto usando a class

$produto->Codigo = 4001;
$produto->Descricao = "CD - The Best of Eric Clapton";
$produto2->Codigo = 4002;
$produto2->Descricao = "CD - Mamonas Assassinas";


$produto->ImprimeEtiqueta(); #funçao para imprimir 
$produto2->ImprimeEtiqueta(); #funçao para imprimir 