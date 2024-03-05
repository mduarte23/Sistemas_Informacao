def media(lista):
    soma = 0
    for e in lista:
        soma = soma + e
    print (lista)
    med = soma/len(lista)
    print(f"A média calculada é {med}")

if __name__=='__main__': #DEIXA EXECUTAR SOMENTE NESSA PAGINA, NÃO IMPORTA PARA OUTRA PAGINA A FUNCAO   

    minha_lista = [1,2,3,4,5]
    print ("Antes de chamar a função")

    media(minha_lista)

    lista2 = [10,20,30,40,50]
    media(lista2)