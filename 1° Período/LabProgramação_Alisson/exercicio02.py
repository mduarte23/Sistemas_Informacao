A= int(input('Escreva valor de A: '))
B= int(input('Escreva o valor de B: '))
C= 0

while A>=B:
    A= A-B
    C= C+1

print (f'Valor de C:{C}')
print (f'Valor de A:{A}')