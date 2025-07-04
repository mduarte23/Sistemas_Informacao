const myModal = new bootstrap.Modal(document.getElementById('modalcadastro'))
var idusuarioatual;

function novo(){
    idusuarioatual = 0;
    document.getElementById('nome').value= "";
    document.getElementById('telefone').value= "";
    document.getElementById('email').value= "";
    myModal.show();
}

function salvar(){
    let nome = document.getElementById('nome').value;
    let telefone = document.getElementById('telefone').value;
    let email = document.getElementById('email').value;

    let usuario = {
        nome: nome,
        telefone: telefone,
        email: email
    };

    let url;
    let metodo;
    if (idusuarioatual > 0){
        //ALTERAR
        url = "http://127.0.0.1:3333/usuario/" + idusuarioatual;
        metodo = "PUT";
    }else{
        //INSERIR
        url = "http://127.0.0.1:3333/usuario";
        metodo = "POST";
    }


    fetch(url, {
        method: metodo, 
        headers: {
            'Content-Type': 'application/json'
        },      
        body: JSON.stringify(usuario)
    }).then(function(){
        //recarrega a lista
        listar();
        //escone o modal
        myModal.hide();
    });
}



function alterar(idusuario){
    idusuarioatual = idusuario;
    fetch('http://127.0.0.1:3333/usuario/'+ idusuarioatual)
    .then(res => res.json())
    .then(dados =>{
        document.getElementById('nome').value = dados.nome;
        document.getElementById('telefone').value = dados.telefone;
        document.getElementById('email').value = dados.email;
        myModal.show();
    });
    

}


function excluir(idusuario){
    fetch('http://127.0.0.1:3333/usuario/' + idusuario, {
        method: 'DELETE',       

    }).then(function(){
        //recarrega a lista
        listar();
    });
}

function listar(){
    const lista = document.getElementById('lista');
    lista.innerHTML = '<tr><td colspan="5">Carregando...</td></tr>';

    fetch('http://127.0.0.1:3333/usuario')
    .then(res => res.json())
    .then(dados => mostrar(dados));
}

function mostrar(dados){
    const lista = document.getElementById('lista');
    lista.innerHTML = '';

    for (let i in dados){
        lista.innerHTML +=  "<tr>" +
                            "<td>" + dados[i].idusuario + "</td>" +
                            "<td>" + dados[i].nome + "</td>" +
                            "<td>" + dados[i].telefone + "</td>" +
                            "<td>" + dados[i].email + "</td>" +
                            "<td>" +
                            "<button type='button' class='btn btn-warning' onclick='alterar("+dados[i].idusuario+")'>Alterar</button>" +
                            "<button type='button' class='btn btn-danger' onclick='excluir("+dados[i].idusuario+")'>Excluir</button>" +
                            "</td>" +
                            "</tr>";
    }
}

