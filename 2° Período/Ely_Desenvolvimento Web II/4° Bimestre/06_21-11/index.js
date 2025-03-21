var itens = [];
abrir();

function inserir(){
    var nome = document.getElementById("nome");
    var telefone = document.getElementById("telefone");
    var email = document.getElementById("email");

    var pessoa = {};  //Cria um novo OBJETO
    pessoa.nome = nome.value;
    pessoa.telefone = telefone.value;
    pessoa.email = email.value;

    itens.push(pessoa);
    //limpa o imput após adicionar o item
    nome.value = "";
    telefone.value = "";
    email.value = "";
    //coloca o foco do cursor no campo
    nome.focus();
    listar();//aciona a funcao listar()
    salvar();
}
function listar(){
    var tab = document.getElementById("tabela");
    tab.innerHTML=""; //Limpa a tabela
    //Montar o titulo da tabela
    tab.innerHTML += "<th>Nome</th><th>Telefone</th><th>E-mail</th><th>Excluir</th>";

    for (var i in itens){
        tab.innerHTML += "<tr><td>"
                      + itens[i].nome 
                      + "</td><td>" 
                      + itens[i].telefone
                      + "</td><td>"
                      + itens[i].email
                      + "</td><td>"
                      + "<a onclick='excluir("+i+")'>X</a>" 
                      + "</td></tr>";
    }

}
function excluir(i){
    itens.splice(i,1);
    listar();
    salvar();
}

function salvar(){
    //converte os dados em uma String JSON
    var dados = JSON.stringify(itens);
    //salva os dados no localstorage
    localStorage.setItem("dados",dados);
}
function abrir(){
    //lê os dados do localStorage
    var dados = localStorage.getItem("dados");
    //converte a String JSON em vetor novamente
    itens = JSON.parse(dados);
    //recarrega os dados
    listar();
}