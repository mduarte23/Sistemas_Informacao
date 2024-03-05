#11- Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se houve lucro, prejuízo ou empate para cada produto. Informe a média de preço de custo e do preço de venda.
m_custo = 0
m_venda = 0

for x in range (40):
    custo = float(input('Informe o preço de custo do produto: R$'))
    venda = float(input('Informe o preço de venda do produto: R$'))
    if custo > venda:
        print('Prejuízo')
    elif custo < venda:
        print ('Lucro')
    else:
        print ('Empate')
    m_custo = m_custo + custo
    m_venda = m_venda + venda

media_c = m_custo / 40
media_v = m_venda / 40
print (f'A média do preço de custo foi R${media_c:.2f} e a média do preço de venda foi R${media_v:.2f}')
