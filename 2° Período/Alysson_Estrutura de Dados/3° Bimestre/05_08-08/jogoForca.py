segredo = "CANETA".strip().upper()#remove os espaços
acerto = []
erros = []
for _ in range (len(segredo)):
    acerto.append('_')
while '_' in acerto:    
    chute = input('Qual a letra: ').upper()
    posicao = 0
    for letra in segredo:
        if chute == letra:
            acerto[posicao] = chute
        posicao +=1
    if (chute not in acerto) and (chute not in erros):
        erros.append(chute)
    posicao +=1

    print(f'Acertos {acerto}')
    print (f'Erros {erros}')
    if len(erros) > 10:
        print ("Enforcou! Game Over")
        break

if len(erros) <= 10:
    print ('Você acertou a palavra!!!')


