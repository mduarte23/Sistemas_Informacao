var itens = [];
abrir();
function inserir(){
    var nome = document.getElementById("nome");
    var idade = document.getElementById("idade");
    var endereco = document.getElementById("endereco");
    var setor = document.getElementById("setor");
    var funcao = document.getElementById("funcao");

    var funcionario = {};

    funcionario.nome = nome.value;
    funcionario.idade = idade.value;
    funcionario.endereco = endereco.value;
    funcionario.setor = setor.value;
    funcionario.funcao = funcao.value;

    //Verificar se os dados foram preenchidos
    if (funcionario.nome == "") {
        window.alert("Preencha os campo Nome")
    }else if (funcionario.idade == ""){
        window.alert("Preencha os campo Idade")
    }
    else if (funcionario.endereco == ""){
        window.alert("Preencha os campo Endereço")
    }else if (funcionario.setor == ""){
        window.alert("Preencha os campo Setor")
    }else if (funcionario.funcao == ""){
        window.alert("Preencha os campo Função")
    }
    else{
        itens.push(funcionario);

        nome.value = "";
        idade.value = "";
        endereco.value = "";
        setor.value = "";
        funcao.value = "";

        nome.focus();

        listar();
        salvar();
    }
    
}

function listar(){
    //var x = document.getElementById("x")
    var tabela = document.getElementById("tabela");
    tabela.innerHTML="";
    //x.src = "img/panda.jpg"

    tabela.innerHTML += "<th>Nome</th><th>Idade</th><th>Endereço</th><th>Setor</th><th>Função</th><th>Excluir</th>"
    for (var i in itens){
        tabela.innerHTML += "<tr><td>"
                         + itens[i].nome
                         +"</td><td>"
                         +itens[i].idade
                         +"</td><td>"
                         +itens[i].endereco
                         +"</td><td>"
                         +itens[i].setor
                         +"</td><td>"
                         +itens[i].funcao
                         +"</td><td>"
                         + "<img class='x' src='img/x.jpg' onclick='excluir("+i+")'/>" 
                         +"</td></tr>"
    }
   
}

function excluir(i){
    itens.splice(i,1);
    listar();
    salvar();
}

function salvar(){
    var dados = JSON.stringify(itens);
    localStorage.setItem("dados",dados);
}

function abrir(){
    var dados = localStorage.getItem("dados");
    itens = JSON.parse(dados);
    listar();
}


