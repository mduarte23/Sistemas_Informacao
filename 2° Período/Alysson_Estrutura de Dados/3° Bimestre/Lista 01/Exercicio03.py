"""3- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) aparece pela primeira vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1"""

lista = []
for x in range (5):
    x = int(input("Digite o valor para inserir no vetor: "))
    lista.append(x)
procure = int(input('Digite o valor que deseja pesquisar: '))

if procure in lista:
    print (f'O elemento esta na posição {lista.index(procure)}')
else:
    print('O elemento não esta na lista. [-1]')