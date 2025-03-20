function definir(){
    var nome = document.getElementById("nome").value;
    var etaria = document.getElementById("etaria");
    var idade = etaria.options[etaria.selectedIndex].text;
    var resp = document.getElementById("resp");

    if (idade == "Abaixo de 14 anos"){
        resp.innerHTML = nome + " pertence a categoria mirim"
    }
    else if (idade == "Entre 14 e 15 anos"){
        resp.innerHTML = nome + " pertence a categoria infaltil"
    }
    else if (idade == "Entre 16 e 17 anos"){
        resp.innerHTML = nome + " pertence a categoria juvenil"
    }
    else if (idade == "De 18 à 20 anos" ){
        resp.innerHTML = nome + " pertence a categoria juniores"
    }
    else if (idade == "Acima de 20 anos"){
        resp.innerHTML = nome + " pertence a categoria profissional"
    }
}
function limpar(){
    var nome = document.getElementById("nome");
    var resp = document.getElementById("resp");
   
    nome.value = "";
    resp.innerHTML = "";
    nome.focus();
}