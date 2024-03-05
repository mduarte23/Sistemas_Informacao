import random

numero = random.randint(1,100)
contador = 0
while True:
    palpite = int(input("Digite um número entre 1 e 100: ")) 
    if palpite == numero:
        contador+=1
        print("Parabéns! Você acertou o número!")
        print(f'O numero de tentativas foi {contador}')
        break
    elif palpite > numero:
        print("O número é MENOR. Tente novamente.")
        print('-'*35)
        contador+=1
    else:
        print("O número é MAIOR. Tente novamente.")
        print('-'*35)
        contador+=1