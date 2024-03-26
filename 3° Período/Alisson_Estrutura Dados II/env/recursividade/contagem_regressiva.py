def contagem_regressiva (n):
    #caso base - caso parada
    if n == 0:
        print ("Fogo")
    else:
        print (n)
        #chamada recursiva - funcao chama ela mesma
        return contagem_regressiva(n-1)

if __name__ == '__main__': #executa o codigo a partir daqui 
    contagem_regressiva(10)