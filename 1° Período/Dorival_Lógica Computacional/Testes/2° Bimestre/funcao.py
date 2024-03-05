# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 19:11:20 2023

@author: marce
Função é um conjunto de instruções (comandos) que executam alguma tarefa.
É definida (criada) através da palavra reservada "def"
"""
def cumprimente(nome):
    print(f'Olá {nome}, como vai você?')

def risco():
    print ('-'*30)
    
risco()
cumprimente ('Zezinho')
risco()
cumprimente  ('Chaves')
risco()
cumprimente ('Sr. Madruga')
risco()
cumprimente ('Bob Esponja')

