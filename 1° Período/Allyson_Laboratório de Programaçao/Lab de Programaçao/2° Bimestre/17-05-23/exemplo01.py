"""
Faça a tabela de multiplicação de numeros de 1 a 10
(ex.: 1 x 1 = 2 ; 1 x 2 = 2...)"""

for primeiro in range (1,11):
    print ('='*15)
    print (f'Tabuada do {primeiro}')
    for segundo in range (1,11):
        resultado= primeiro * segundo
        print (f'{primeiro} x {segundo}\t= {resultado}')
