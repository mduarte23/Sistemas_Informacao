valor=int(input('Digite um númer entre 0 e 9999: '))

if valor >=0 and valor <= 9999:
    milhar= valor // 1000
    resto = valor % 1000
    centena = resto // 100
    resto = resto % 100
    dezena= resto // 10
    unidade = resto % 10
    if milhar == 9:
        print ('nove mil', end=' ') #end imprime e deixa espaço, nao quebra linha
    elif milhar == 8:
        print ('oito mil', end=' ')
    elif milhar == 7:
        print ('sete mil', end=' ')
    elif milhar == 6:
        print ('seis mil', end=' ')
    elif milhar == 5:
        print ('cinco mil', end=' ')
    elif milhar == 4:
        print ('quatro mil', end=' ')
    elif milhar == 3:
        print ('tres mil', end=' ')
    elif milhar == 2:
        print ('dois mil', end=' ')
    elif milhar == 1:
        print ('um mil', end=' ')

    if milhar % 1000 != 0:
        print ('e', end=' ')


    if centena == 9:
        print ('novecentos', end=' ')
    elif centena == 8:
        print ('oitocentos', end=' ')
    elif centena == 7:
        print ('setecentos', end=' ')
    elif centena == 6:
        print ('seiscentos', end=' ')
    elif centena == 5:
        print ('quinhentos', end=' ')
    elif centena == 4:
        print ('quatrocentos', end=' ')
    elif centena == 3:
        print ('trezentos', end=' ')
    elif centena == 2:
        print ('duzentos', end=' ')
    elif centena == 1:
        if (centena % 100) == 0:
            print ('cem')
        else:
            print ('cento', end=' ')

    if centena % 100 != 0:
        print ('e', end=' ')
    
    if dezena == 9:
        print (' noventa', end=' ')
    elif dezena == 8:
        print ('oitenta', end=' ')
    elif dezena == 7:
        print ('setenta', end=' ')
    elif dezena == 6:
        print ('sessenta', end=' ')
    elif dezena == 5:
        print ('cinquenta', end=' ')
    elif dezena == 4:
        print ('quarenta', end=' ')
    elif dezena == 3:
        print ('trinta', end=' ')
    elif dezena == 2:
        print ('vinte', end=' ')
    elif dezena == 1:
        print ('dez', end=' ')

    if dezena % 10 !=1:
        print ('e', end=' ')

    if unidade == 9:
        print ('nove')
    elif unidade == 8:
        print ('oito')
    elif unidade == 7:
        print ('sete')
    elif unidade == 6:
        print ('seis')
    elif unidade == 5:
        print ('cinco')
    elif unidade == 4:
        print ('quatro')
    elif unidade == 3:
        print ('tres')
    elif unidade == 2:
        print ('dois')
    elif unidade == 1:
        print ('um')




 
else:
    print('Você digitou um valor fora do intervalo.')

