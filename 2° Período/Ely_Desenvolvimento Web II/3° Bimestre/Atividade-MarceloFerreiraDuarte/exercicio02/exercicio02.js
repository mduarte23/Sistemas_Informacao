function calcular(){
    var nome = document.getElementById("nome").value;
    var nascimento = Number(document.getElementById("nascimento").value);
    var resp = document.getElementById("resp");
    var ano = 2023 - nascimento;

    if (ano < 14){
        resp.innerHTML = nome +" é Mirim"
    }
    else if (ano <= 15){
        resp.innerHTML = nome +" é Infantil"
    }
    else if (ano <= 17){
        resp.innerHTML = nome +" é Juvenil"
    }
    else if (ano <= 20){
        resp.innerHTML = nome +" é Juniores"
    }
    else{
        resp.innerHTML = nome +" é Profissional"
    }
}
function limpar(){
    var nome = document.getElementById("nome");
    var nascimento = document.getElementById("nascimento");
    var resp = document.getElementById("resp");

    nome.value = ""
    nascimento.value = "";
    resp.innerHTML= "";
    nome.focus();
}