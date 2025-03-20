def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0) # posicionando cursor no inicio
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor =  float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("D:\\Sistemas de Informaçao\\2° Período\Alysson_Estrutura de Dados\\4° Bimestre\E_D\\07_16-11\\entrada.txt")
    print(valores)
    return sum(valores)

# EXERCICIOS 16/11/2023 
def maior_valor_arquivo():
    valores = leitura("D:\\Sistemas de Informaçao\\2° Período\Alysson_Estrutura de Dados\\4° Bimestre\E_D\\07_16-11\\entrada.txt") 
    return max(valores)

def multiplica_valores_arquivo():
    valores = leitura("D:\\Sistemas de Informaçao\\2° Período\Alysson_Estrutura de Dados\\4° Bimestre\E_D\\07_16-11\\entrada.txt")
    temp = 1
    for i in valores:
        temp = temp * i
    return temp

if __name__ == '__main__':
    resultado = soma_valores_arquivo()
    print("Soma")
    print(resultado)
    print ("Maior valor")
    maior = maior_valor_arquivo()
    print (maior)
    multiplicacao = multiplica_valores_arquivo()
    print ("Multiplicação")
    print (multiplicacao)