function calcular(){
    var nota1 = Number(document.getElementById("nota1").value);
    var nota2 = Number(document.getElementById("nota2").value);
    var resp = document.getElementById("resp");

    media = (nota1 + nota2)/2;

    if (media >= 70){
        resp.innerHTML = "Aprovado";
    }
    else if (media < 40){
        resp.innerHTML = "Reprovado";
    }
    else {
        resp.innerHTML = "Prova Final"
    }
}
function limpar(){
    var nota1 = document.getElementById("nota1");
    var nota2 = document.getElementById("nota2");
    var resp = document.getElementById("resp");

    nota1.value = "";
    nota2.value = "";
    resp.innerHTML = "";
    nota1.focus();
}