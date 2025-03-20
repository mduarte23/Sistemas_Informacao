function calcular(){
    var reta1 = Number(document.getElementById("reta1").value);
    var reta2 = Number(document.getElementById("reta2").value);
    var reta3 = Number(document.getElementById("reta3").value);
    var resp = document.getElementById("resp");

    if ((reta1 < (reta2 + reta3)) || (reta2 < (reta1 + reta3)) || (reta3 < (reta1 + reta2))){
        if ((reta1 == reta2) && (reta1  == reta3)){
            resp.innerHTML = "Triângulo Equilátero"
        }
        else if ((reta1 == reta2) || (reta2 == reta3) || (reta1 == reta3)){
            resp.innerHTML = "Triângulo Isósceles"
        }
        else{
            resp.innerHTML = "Triângulo Escaleno"
        }
    }
    else{
        resp.innerHTML = "Não é possivel montar um triângulo com essas retas"
    }
}
function limpar(){
    var reta1 = document.getElementById("reta1");
    var reta2 = document.getElementById("reta2");
    var reta3 = document.getElementById("reta3");
    var resp = document.getElementById("resp")

    reta1.value = "";
    reta2.value = "";
    reta3.value = "";
    resp.innerHTML = "";
    reta1.focus();
}