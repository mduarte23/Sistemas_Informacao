<?php

//Às vezes, você pode ter que lidar com datas em formatos diferentes. Nesse caso, você pode usar o método createFromFormat() da classe DateTime para criar um novo objeto DateTime a partir de uma string de data em um formato específico.


$date1 = DateTime::createFromFormat('d/m/Y', '01/07/2023');
$date2 = DateTime::createFromFormat('d/m/Y H:i:s','10/07/2023 15:00:00'); #define formato de data e hora

$interval = $date1->diff($date2);

echo $interval->days;