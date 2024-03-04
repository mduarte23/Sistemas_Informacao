"""
Projeto: Adivinhe o número

Descrição: Neste jogo, o programa escolhe aleatoriamente um número entre 1 e 100. O jogador deve tentar adivinhar o número correto dentro de um número limitado de tentativas.

Regras:

O programa escolhe um número aleatório entre 1 e 100.
O jogador tem no máximo 10 tentativas.
O jogador faz uma suposição fornecendo um número.
O programa informa ao jogador se o número correto é maior ou menor do que a suposição feita.
O jogador continua fazendo suposições até adivinhar corretamente o número ou esgotar o número de tentativas.
Funcionalidades adicionais:

No início do jogo, o programa exibe uma mensagem de boas-vindas e explica as regras do jogo.
O programa mantém um registro do número de tentativas do jogador.
Ao final do jogo, o programa informa se o jogador adivinhou corretamente o número ou não, e exibe o número de tentativas realizadas.
O programa pergunta se o jogador deseja jogar novamente.
Dicas:

Você pode usar a biblioteca random em Python para gerar o número aleatório.
Utilize estruturas de controle como loops e condicionais para implementar a lógica do jogo.
Lembre-se de validar a entrada do jogador, garantindo que seja um número dentro do intervalo correto."""

import random
import os

opcao = 'S'
os.system('cls')
print('Bem vindo ao nosso jogo, aqui você irá tentar acertar o número gerado aleatóriamente entre 1 e 100, você tem 10 tentativas, a cada erro você terá uma dica se o número á maior ou menor que o número que digitou.')
print ('-'* 50)
while opcao == 'S':
    vida= 9
    numero = random.randint(1,100)
    errado= []
    tentativa = 1
    palpite = int(input('Digite um número entre 1 e 100: '))
    
    while palpite != numero and vida > 0:
        while palpite in errado:
            palpite = int(input('Número ja digitado, tente outro número: '))
        while palpite <= 0 or palpite > 100:
            palpite = int (input('Número invalido, tente um número entre 1 e 100: '))
        os.system('cls')
        errado.append(palpite)
        print (f'Você ainda tem {vida} tentativas')
        print (f'Números já digitados: {errado}')
        tentativa += 1
        vida -= 1
        if palpite > numero:            
            print (f'O número {palpite} é maior que o número sorteado')
            palpite = int(input('Digite outro número: '))
        else:            
            print(f'O número {palpite} é menor que o número sorteado')    
            palpite = int(input('Digite outro número: '))
    os.system('cls')       
    if palpite == numero:
        print (f'PARABÉNS!!! Você acertou o númmero {numero} com {tentativa} tentativas.')
    else:
        print (f'Que pena, suas vidas acabaram. O número era {numero}.') 
    opcao = input('Deseja jogar novamente? "S" ou "N": ').upper()
    while opcao != 'S' and opcao != 'N':
        opcao = input('Opção inválida, tente novamente: ').upper()
    os.system('cls')
    if opcao == 'N':
        print('Obrigado por utilizar o sistema.')
