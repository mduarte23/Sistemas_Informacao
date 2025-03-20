function calcular(){
    var numero1 = Number(document.getElementById("numero1").value);
    var numero2 = Number(document.getElementById("numero2").value);
    var operacao = document.getElementById("operacao");
    var op = operacao.options[operacao.selectedIndex].text;
    var resp = document.getElementById("resp");

    if (op == "Adição"){
        var resultado = numero1 + numero2;
        resp.innerHTML= "Operação de adição, e o resultado é: " + resultado;
    }
    else if (op == "Subtração"){
        resultado = numero1 - numero2;
        resp.innerHTML= "Operação de subtraçao, e o resultado é: " + resultado;
    }
    else if (op == "Multiplicação"){
        resultado = numero1 * numero2
        resp.innerHTML= "Operação de multiplicação, e o resultado é: " + resultado;
    }
    else if (op == "Divisão"){
        resultado = numero1 / numero2
        resp.innerHTML= "Operação de multiplicação, e o resultado é: " + resultado;
    }
    else if (op == "Resto"){
        resultado = numero1 % numero2
        resp.innerHTML= "Operação de resto, e o resultado é: " + resultado;
    }
}
function limpar(){
    var numero1 = document.getElementById("numero1");
    var numero2 = document.getElementById("numero2");
    var resp = document.getElementById("resp")

    numero1.value="";
    numero2.value="";
    resp.innerHTML="";
    numero1.focus();
}