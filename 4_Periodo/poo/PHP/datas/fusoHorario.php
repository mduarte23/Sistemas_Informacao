<?php

//Se as datas que você está manipulando estão em fusos horários diferentes, você deve levar isso em consideração ao calcular a diferença entre elas.

$date1 = new DateTime("2023-07-01", new DateTimeZone('America/New_York')); #Define a data com o fuso horario local
$date2 = new DateTime('2023-07-10', new DateTimeZone('Europe/Paris'));

$interval = $date1->diff($date2);

echo $interval->days;