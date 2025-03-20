

function voltar(){
    var camiseta = document.getElementById("camiseta");
    if (camiseta.src.includes("azulcorpo.jpg")){
        camiseta.src = "img/azulfrente.jpg";
    }
    else if (camiseta.src.includes("brancacorpo.jpg")){
        camiseta.src = "img/brancafrente.jpg";
    }
    else if (camiseta.src.includes("bermudaa2.jpg")){
        camiseta.src = "img/bermudaa1.jpg";
    }
    else if (camiseta.src.includes("bermudab2.jpg")){
        camiseta.src = "img/bermudab1.jpg";
    }

}
function avancar(){
    var camiseta = document.getElementById("camiseta");
    if (camiseta.src.includes("azulfrente.jpg")){
        camiseta.src = "img/azulcorpo.jpg";
    }
    else if (camiseta.src.includes("brancafrente.jpg")){
        camiseta.src = "img/brancacorpo.jpg";
    }
    else if (camiseta.src.includes("bermudaa1.jpg")){
        camiseta.src = "img/bermudaa2.jpg";
    }
    else if (camiseta.src.includes("bermudab1.jpg")){
        camiseta.src = "img/bermudab2.jpg";
    }
    
}

function azul(){
    var camiseta = document.getElementById("camiseta");
    if (camiseta.src.includes("azulfrente.jpg")){
        camiseta.src = "img/azulfrente.jpg";
    }
    else if (camiseta.src.includes("azulcorpo.jpg")){
        camiseta.src = "img/azullfrente.jpg";
    }
    else if (camiseta.src.includes("bermudab1.jpg")){
        camiseta.src = "img/bermudaa1.jpg";
    }
    else if (camiseta.src.includes("bermudab2.jpg")){
        camiseta.src = "img/bermudaa1.jpg";
    }
    else if (camiseta.src.includes("bermudaa2.jpg")){
        camiseta.src = "img/bermudaa1.jpg";
    }
    else if (camiseta.src.includes("bermudaa1.jpg")){
        camiseta.src = "img/bermudaa1.jpg";
    }
    else if (camiseta.src.includes("brancocorpo.jpg")){
        camiseta.src = "img/azullfrente.jpg";
    }
    else if (camiseta.src.includes("brancofrente.jpg")){
        camiseta.src = "img/azullfrente.jpg";
    }
}
function branca(){
    var camiseta = document.getElementById("camiseta");
    camiseta.src = "img/brancafrente.jpg"
}
function camiseta(){
    var camiseta = document.getElementById("camiseta");
    camiseta.src = "img/azulfrente.jpg";
}
function bermuda(){
    var camiseta = document.getElementById("camiseta");
    camiseta.src = "img/bermudaa1.jpg";
}
