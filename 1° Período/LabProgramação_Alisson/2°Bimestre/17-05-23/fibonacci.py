"""Faça um programa para calcular a série de fibonacci para um número informado pelo usuário sendo F(0) = 0,
F(1)= 1 e F(n)= F(n-1)+F(n-2)
Por exemplo 0,1,1,2,3,5,8,13,21,34
"""
qtd=int(input('Digite até a posição desejada da sequencia Fibonacci: '))

a= 0
b = 1
contador= 2
if qtd >= 0:
    print(a, end=', ')
if qtd >= 1:
    print(b, end=', ')
    
for x in range(2,qtd+1):
    
    c = a + b
    a = b
    b = c
    contador +=1
    if contador <= qtd:
        print(c, end=', ')
    else:
        print(c, end=' ')

    
    
