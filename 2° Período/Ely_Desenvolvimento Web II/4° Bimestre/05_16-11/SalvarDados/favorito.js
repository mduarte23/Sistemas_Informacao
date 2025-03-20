let lblEsporte = document.getElementById("lblEsporte");
let btnExcluir = document.getElementById("btnExcluir");

window.onload = mostrar;
btnExcluir.addEventListener("click", excluir);

function mostrar(){
    if (localStorage.getItem("esporte") != null){
        lblEsporte.innerHTML = localStorage.getItem("esporte");
    }else{
        lblEsporte.innerHTML = "nenhum esporte salvo";
    }
}
function excluir(){
    localStorage.removeItem("esporte");
    lblEsporte.innerHTML = "Esporte excluido";
}