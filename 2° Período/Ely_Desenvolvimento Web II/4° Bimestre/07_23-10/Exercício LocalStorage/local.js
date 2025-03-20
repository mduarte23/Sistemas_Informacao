var itens = [];
function inserir(){
    var nome = document.getElementById ("nome");
    var preco = document.getElementById ("preco");
    var produto = {};
    produto.nome = nome.value;
    produto.preco = preco.value;
    itens.push(produto);
    nome.value = "";
    preco.value = "";
    nome.focus();
    salvar();
}
function voltar(){
    var nome = document.getElementById ("nome").value;
    var preco = document.getElementById ("preco").value;
    var resp = document.getElementById ("resp");
    resp.innerHTML = "Nome do produto:" + nome + " , preço do produto: " + "R$"+preco+",00" 
    inserir();
    salvar();
}
function salvar(){
    var dados = JSON.stringify(itens);
    localStorage.setItem("dados", dados);  
}