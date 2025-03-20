#'1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova

matriz = []
contador = 0
qtd = 10
while contador < qtd:
    linha = []
    nome = input("Digite o nome: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    linha.append(nome)
    linha.append(idade)
    matriz.append(linha)
    contador += 1

novo = matriz[0][0]
menor = matriz[0][1]

for i in range (contador):
    if menor > matriz[i][1]:
        novo = matriz[i][0]
        menor = matriz[i][1]
    
print (f"A pessoa mais nova é {novo} com idade de {menor} anos")
        

    