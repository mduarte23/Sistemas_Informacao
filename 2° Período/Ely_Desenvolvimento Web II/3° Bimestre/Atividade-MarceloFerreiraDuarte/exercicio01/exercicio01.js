function calcular(){
    var gasolina = Number(document.getElementById("gasolina").value);
    var etanol = Number(document.getElementById("etanol").value);
    var resp = document.getElementById("resp");
    var calculo = gasolina * 0.7;

    if (etanol < calculo){
        resp.innerHTML = "Está compensando abastecer com etanol"
    }
    else{
        resp.innerHTML = "Está compensano abastecer com gasolina"
    }
}
function limpar(){
    var gasolina = document.getElementById("gasolina");
    var etanol = document.getElementById("etanol");
    var resp = document.getElementById("resp");

    gasolina.value = "";
    etanol.value = "";
    resp.innerHTML = "";
    gasolina.focus();
}