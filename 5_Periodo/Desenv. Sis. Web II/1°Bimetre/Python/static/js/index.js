function entrar(){
    let email = document.getElementById('email').value;
    let senha = document.getElementById('senha').value;

    fetch ("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email, senha: senha})
        .then(res => {
            if (!res.ok){
                alert("Login Inválido");
                return null;
            } else {
                return res.json();
            }
        })
        .then(dados => {
            if (dados != null){
                // Salva o token no seesionStorage
                sessionStorage.setItem("token", dados.token);
                // redireciona para uma pagina
                window.location.href = "usuario.html";
            }
        })
    })
}