# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:22:32 2023

@author: marce
"""
"""
x = 'Oi, como você vai?'
msg= '/ ' + x + ' /'
print ('-'*len(msg)) #coloca - o tanto de caracteres do {msg}
print(msg)
print ('-'*len(msg)) # len conta a quantidade de itens da variavel

x = 'E aí?'
msg= '/ ' + x + ' /'
print ('-'*len(msg))
print(msg)
print ('-'*len(msg))

x = 'nãoconsigolernada, naoconsigolernada'
msg= '/ ' + x + ' /'
print ('-'*len(msg))
print(msg)
print ('-'*len(msg))

x = input('Qual a sua mensagem? ')
msg= '/ ' + x + ' /'
print ('-'*len(msg))
print(msg)
print ('-'*len(msg))
"""
def mensagem(x):
    msg='/ '+ x + ' /'
    print ('-'*len(msg))
    print(msg)
    print('-'*len(msg))

mensagem('Oi, como vai você?')
mensagem('E aí?')
mensagem('obabaoobabaoobabao')
mensagem(input('Qual a sua mensagem? '))

