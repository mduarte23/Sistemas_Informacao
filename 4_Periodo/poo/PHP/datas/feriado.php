<?php

//Muitas vezes, para cálculos relacionados ao mundo empresarial e comercial, queremos excluir não apenas os finais de semana, mas também os feriados.

function isHoliday ($date, $holidays){
    $formatDate = $date->format('Y-m-d');
    if(in_array($formatDate, $holidays)){
        return true;
    } else{
        return false;
    }
}

$holidays = ['2023-07-04', '2023-12-25']; #define os dias que sao feriados
$date1 = new DateTime('2023-07-01');
$date2 = new DateTime('2023-07-31');

$interval = new DateInterval('P1D');
$dates = new DatePeriod($date1, $interval, $date2);

$weekendDays = 0;
$holidayDays= 0;

foreach($dates as $date){
    if ($date->format('N')>=6){  #confere se o dia é fim de semana
        $weekendDays++;
    }
    if(isHoliday($date, $holidays)){ #confere se o dia é feriado
        $holidayDays++;
    }
}

$allDays = $date2->diff($date1)->days;
$businessDays = $allDays - $weekendDays - $holidayDays;

echo $businessDays;