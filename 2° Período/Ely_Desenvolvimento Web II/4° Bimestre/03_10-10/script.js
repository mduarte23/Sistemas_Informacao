function carregarProduto(){
    var m = document.getElementById("marca");
    var marca = m.options[m.selectedIndex].text;
    var prod = document.getElementById("produto");

    if (marca == "Aplle"){
        prod.innerHTML = "<option></option>";
        prod.innerHTML += "<option>IPhone</option>";
        prod.innerHTML += "<option>IPad</option>";
        prod.innerHTML += "<option>MacBook</option>";
    }
    else if (marca == "Samsung"){
        prod.innerHTML = "<option></option>";
        prod.innerHTML += "<option>Galaxy S20</option>";
        prod.innerHTML += "<option>Galaxy S21</option>";
        prod.innerHTML += "<option>Galaxy Tab</option>";
    }
    else if (marca == "Xiaomi"){
        prod.innerHTML = "<option></option>";
        prod.innerHTML += "<option>Redmi 11</option>";
        prod.innerHTML += "<option>Redmi 12</option>";
        prod.innerHTML += "<option>Redmi Note</option>";
    }
}
function carregarPreco(){
    var prod = document.getElementById("produto");
    var produto = prod.options[prod.selectedIndex].text;
    var preco = document.getElementById("precoUnit");
    
    if (produto == "IPhone"){
        preco.innerHTML += "4.000,00"
    }
    else if (produto == "IPad"){
        preco.innerHTML += "6.500,00"
    }
    else if (produto == "MacBook"){
        preco.innerHTML += "8.000,00"
    }
    else if (produto == "Galaxy S20"){
        preco.innerHTML += "2.900,00"
    }
    else if (produto == "Galaxy S21"){
        preco.innerHTML += "2.000,00"
    }   
    else if (produto == "Galaxy Tab"){
        preco.innerHTML += "2.800,00"
    }  
    else if (produto == "Redmi 11"){
        preco.innerHTML += "1.000,00"
    }   
    else if (produto == "Redmi 12"){
        preco.innerHTML += "1.200,00"
    }  
    else if (produto == "Redmi Note"){
        preco.innerHTML += "2.400,00"  
    } 

    function precoTotal(){
        var qtd = Number(document.getElementById("qtd").value);
        var precoUnit = Number(document.getElementById("precoUnit"));
        var precoTotal = document.getElementById("precoTotal");

        var total = qtd * precoUnit;

        precoTotal.innerHTML += "R$" + total;

    }
}
