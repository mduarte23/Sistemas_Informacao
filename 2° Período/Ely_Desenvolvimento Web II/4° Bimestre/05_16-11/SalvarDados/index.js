let txtEsporte = document.getElementById("txtEsporte");
let btnOK = document.getElementById("btnOk");

btnOK.addEventListener("click", salvar);

function salvar(){
    if (txtEsporte.value != ""){
        localStorage.setItem("esporte", txtEsporte.value);
        alert ("Esporte salvo com sucesso!");
        location.href="favorito.html";
    }else{ 
        alert("Digite o seu esporte favorito!");
    }
}