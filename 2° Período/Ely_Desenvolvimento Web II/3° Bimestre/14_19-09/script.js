function calcular(){;
    var prod = document.getElementById("produto")
    var produto = prod.options[prod.selectedIndex].text
    var qtd = parseInt(document.getElementById("quantidade").value);
    var dinheiro = document.getElementById("dinheiro").checked;
    var cartao = document.getElementById("cartao").checked;
    var entrega = document.getElementById("entrega").checked;
    var resp = document.getElementById("resp");

    var preco = 0;
    if (produto == "Coca-Cola Lata"){
        preco = 3.50
    }
    else if (produto == "Coxinha"){
        preco = 4.00
    }
    else if (produto == "Pão de Quaijo"){
        preco = 3.00
    }

    var total = preco * qtd;

    if (dinheiro.checked){
        total = total - (total * 0.1)
    }

    if (entrega.checked){
        total = total + 6
    }
    resp.innerHTML = "Valor total R$" + total.toFixed(2);
}