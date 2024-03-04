"""Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e
divisão dos números lidos.
"""

numero1  =  int ( input ( 'Digito ou 1° numero: ' ))
numero2  =  int ( input ( 'Digito ou 2° numero: ' ))

soma  =  numero1 + numero2
subtracao =  numero1 - numero2
multiplicacao =  numero1 * numero2
divisão =  numero1 / numero2

print ( f'Os resultados são: \n Soma: { soma } \n Subtração: { subtracao } \n Multiplicação: { multiplicacao } \n Divisão: { divisão } ' )