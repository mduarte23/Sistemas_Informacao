<?php

//A classe DateTime do PHP fornece uma maneira orientada a objetos de trabalhar com datas e horas.

$date1 = new DateTime("2023-07-01"); #data 1
$date2 = new DateTime("2023-07-10"); #data 2

$interval = $date1->diff($date2); #diff calcula a diferenca entre as duas datas

echo $interval->days; #defie o formado para dias