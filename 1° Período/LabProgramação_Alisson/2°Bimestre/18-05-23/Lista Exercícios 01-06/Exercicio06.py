#6-Escrever um algoritimo que lê o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação.
#MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME)/ 7
#A atribuição de conceitos obedece a tabela abaixo:

#Média de Aproveitamento | Conceito
#MA >= 9,0               | A
#7,5 <= MA < 9,0         | B
#6,0 <= MA < 7,5         | C 
#4,0 <= MA < 6,0         | D 
#MA < 4,0                | E 

#O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem: APROVADO se o conceito for A, B ou C e REPROVADO se o conceito for D ou E. Pergunte se o usuário deseja digitar as notas de outro aluno S para sim e N para não

opcao = 'S'
while opcao == 'S':
    identificacao= int(input('Digite o número de identificação do aluno: '))
    nota1= float(input('Digite a nota da prova 1: '))
    nota2=float(input('Digite a nota da prova 2: '))
    nota3= float(input('Digite a nota da prova 3: '))
    exercicios= float(input('Digite a nota dos exercícios: '))

    media= (nota1 + (nota2 * 2) + (nota3 * 3) + exercicios) / 7

    if media >= 9:
        nota = 'A'
    elif media >= 7.5:
        nota = 'B'
    elif media >= 6:
        nota = 'C'
    elif media >= 4:
        nota = 'D'
    else:
        nota = 'E'

    if nota == 'A' or nota == 'B' or nota == 'C':
        final= 'APROVADO'
    else:
        final = 'REPROVADO'


    
    print(f'O aluno(a) {identificacao} teve obteve as notas {nota1} na 1° prova, nota {nota2} na 2° prova, nota {nota3} na 3° prova e nota {exercicios} nos exercícios, obteve a média {media :.2f}, com conceito {nota} e foi {final}.')

    opcao = input('Deseja calcular a nota de outro aluno? (S)sim / (N)não: ')
    while opcao != 'S' and opcao != 'N':
        opcao = input('Opção invalida, tente novamente (S) ou (N): ')

