<?php

//Em algumas situações, pode ser necessário calcular o número de dias úteis (ou seja, excluindo sábados e domingos) entre duas datas.

$date1 = new DateTime('2023-07-01');
$date2 = new DateTime('2023-07-31');

$interval = new DateInterval('P1D');
$dates = new DatePeriod($date1, $interval,$date2);

$wekeendDays = 0;

foreach ($dates as $date){
    if ($date->format('N') >= 6){
        $wekeendDays++;
    }
}

$allDays = $date2->diff($date1)->days;
$weekDays = $allDays - $wekeendDays;

echo $weekDays;