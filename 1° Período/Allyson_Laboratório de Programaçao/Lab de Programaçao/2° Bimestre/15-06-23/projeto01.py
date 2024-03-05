"""Desenvolva um jogo da forca em Python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. O jogador deve tentar adivinhar a palavra digitando letras. Se a letra estiver na palavra secreta, ela deve ser revelada nas posiçoes corretas. Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador adivinhe corretamente a palavra secreta ou perca todas as vidas. O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma "representação" da forca conforme o jogador erra letras. Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente."""

import os
import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)
palavras = response.text.split('\n')
errada = []
opcao = 'S'

while opcao == 'S':
    secreta = random.choice(palavras).upper() 
    palavra = '*'*len(secreta)
    vidas = 100
    digitadas = ''
    print(palavra)
    while vidas > 0:
        letra = input('Digite uma letra: ').upper()
        if digitadas.find(letra) >= 0:
            print('Letra já digitada, tente outra letra.')
            letra = input('Digite outra letra: ').upper()
        else:
            digitadas += letra

        ### verificar se a letra esta na palavra secreta
        auxiliar =  list(palavra) 
        for i in range(len(secreta)):
            if letra == secreta[i]:
                # achou a letra na palavra secreta
                # palavra
                auxiliar[i] = letra
        
        os.system('cls') #Limpa a tela
        print(palavra)
       
        

        # percorreu todas e nunca achou, dimunui uma vida
        vidas -= 1

