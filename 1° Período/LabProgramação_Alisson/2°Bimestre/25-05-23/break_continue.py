for letra in ('A', 'B', 'C'):
    for i in range (3):
        if i == 1:
            break  #interrompe o for interno
        print (f'{letra} {i}')

for letra in ('A', 'B', 'C'):
    for i in range (3):
        if i == 1:
            continue  #ignora o restante do código e executa a repetição novamente
        print (f'{letra} {i}')