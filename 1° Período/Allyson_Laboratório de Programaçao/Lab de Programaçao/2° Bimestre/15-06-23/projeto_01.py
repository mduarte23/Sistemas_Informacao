import os
import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)
palavras = response.text.split('\n')
opcao = 'S'

while opcao == 'S':
    sorteada = random.choice(palavras).upper()
    print (sorteada)
    palavra = '*'*len(sorteada)
    tentativas = []
    vida = 10
    while vida > 0  and  palavra.count('*') != 0:
        os.system('cls')
        print (palavra)
        print (f'Vidas restantes: {vida}')
        print (f'Letras digitadas erradas:{tentativas}')
        letra = input('Digite uma letra: ').upper()
        while len(letra)>1:
            print('Formato inválido, tente novamente.')
            letra = input('Digite uma letra: ').upper()
        while letra in tentativas or letra in list(palavra):
            print (f'Letra {letra} já foi digitada, tente outra letra.')
            letra = input('Digite uma letra: ').upper()
        auxiliar = list(palavra)
        for x in range(len(sorteada)):
            if letra == sorteada[x]:
                auxiliar[x] = letra
                palavra = ''.join(auxiliar)
                print (palavra)
        if sorteada.count(letra) == 0:
            vida -= 1
            tentativas.append(letra)
            
    if vida == 0:
        os.system('cls')
        print(f'Que pena, você perdeu, a palavra era {sorteada}')
    else:
        os.system('cls')
        print (palavra)
        print('PARABÊNS você ganhou!!!')
    opcao = input('Deseja jogar novamente? "S" ou "N": ').upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida, tente novamente.')
        opcao = input('Deseja jogar novamente? "S" ou "N"').upper()
if opcao == 'N':
    print('Obrigado por ter utilizado nosso sistema!!!')
            
            
            

        
        

