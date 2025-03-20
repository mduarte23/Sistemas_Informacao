function calcular(){
    var idade = document.getElementById("idade").value;
    var resp = document.getElementById("resp");
    if ((idade >= 18)&&(idade <=65)){
        resp.innerHTML = "Voto Obrigatório."
    }
    else if (idade < 16){
        resp.innerHTML = "Não Vota.";
    }
    else{
        resp.innerHTML = "Voto Facultativo.";
    }
}  
function limpar(){
    var idade = document.getElementById("idade");
    var resp = document.getElementById("resp");
    resp.innerHTML= "";
    idade.value="";
    idade.focus();
}