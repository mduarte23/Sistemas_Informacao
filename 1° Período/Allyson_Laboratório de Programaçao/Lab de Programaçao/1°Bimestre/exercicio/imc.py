massa=float(input('Digite o peso em Kg: '))
altura= float(input('Digite a altura em metros: '))

imc= massa/(altura**2)
print (f'IMC= {imc:.1f}')
if imc< 18.5:
    print(f'Esta abaixo do peso.')
elif imc <24.9:
    print ('Está saudável.')
elif imc <29.9:
    print(f'Peso em excesso.')
elif imc <34.9:
    print (f'Obesidade Grau I.')
elif imc <39.9:
    print (f'Obesidade Grau II (severa).')
else:
    print('Obesidade Grau III (mórbida)')