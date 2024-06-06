a = 12
b = 0

try:
    print (a/b)

except ZeroDivisionError as e:
    print (f"Não é possivel realizar divisao por {b}")
    print(e)
else:
    print ('Sem nenhum erro')

finally:
    print ('Aqui sempre vai printar')