try: 
    with open('arquiv.txt', 'r') as file_object:
        texto = file_object.read()
        print(texto)

except FileNotFoundError as e:
    print(e)

# with open('arquiv.txt', 'r') as file_object:
#     texto = file_object.read()
#     print(texto)