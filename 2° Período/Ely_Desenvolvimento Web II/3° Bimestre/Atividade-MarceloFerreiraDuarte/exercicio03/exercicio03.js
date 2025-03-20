var resp = document.getElementById("resp")
var dataAtual = new Date();
var numeroDiaSemana = dataAtual.getDay();

if (numeroDiaSemana == 0){
    resp.innerHTML= "Hoje é Domingo"
}
else if (numeroDiaSemana == 1){
    resp.innerHTML= "Hoje é Segunda-Feira"
}
else if (numeroDiaSemana == 2){
    resp.innerHTML= "Hoje é Terça-Feira"
}
else if (numeroDiaSemana == 3){
    resp.innerHTML= "Hoje é Quarta-Feira"
}
else if (numeroDiaSemana == 4){
    resp.innerHTML= "Hoje é Quinta-Feira"
}
else if (numeroDiaSemana == 5){
    resp.innerHTML= "Hoje é Sexta-Feira"
}
else if (numeroDiaSemana == 6){
    resp.innerHTML= "Hoje é Sábado"
}