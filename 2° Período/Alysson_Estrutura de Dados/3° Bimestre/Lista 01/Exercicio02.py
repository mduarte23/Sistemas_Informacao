"""2- Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor."""

lista = []
qtd = 10
for x in range(qtd):
    numero = int(input(f'Digite o número: '))
    if numero not in lista:
        lista.append(numero)
print (f'Existem {len(lista)} valores diferentes na lista.')
