function calcular(){
    var peso = Number(document.getElementById("peso").value);
    var altura = Number(document.getElementById("altura").value);
    var resp = document.getElementById("resp");

    var imc = peso / (altura ** 2);
    if (imc < 22){
        resp.innerHTML = "IMC " + imc.toFixed(1) + " abaixo do peso"
    }
    else if(imc >= 22 && imc <= 26){
        resp.innerHTML = "IMC " + imc.toFixed(1) + " peso adequado"
    }
    else if (imc > 26 && imc <= 32){
        resp.innerHTML = "IMC " + imc.toFixed(1) + " acima do peso"
    }
    else if (imc > 32){
        resp.innerHTML = "IMC " + imc.toFixed(1) + " obesidade"
    }
};
function limpar(){
    var peso = document.getElementById("peso");
    var altura = document.getElementById("altura");
    var resp = document.getElementById("resp");

    peso.value = "";
    altura.value="";
    resp.innerHTML="";
    peso.focus();
}