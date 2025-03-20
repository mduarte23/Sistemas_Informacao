function calcular(){
    var preco = Number(document.getElementById("preco").value);
    var qtd = Number(document.getElementById("qtd").value);
    var resp = document.getElementById("resp");

    var media = preco * qtd
    if (qtd > 10){
        media = media - (media * 0.1);
        resp.innerHTML = "O valor com desconto será R$" + media.toFixed(2);
    }
    else{
        resp.innerHTML = "O valor será R$" + media.toFixed(2);
    }
}
function limpar(){
    var preco = document.getElementById("preco");
    var qtd = document.getElementById("qtd");
    var resp = document.getElementById("resp");

    preco.value = "";
    qtd.value = "";
    resp.innerHTML = "";
    preco.focus();
}