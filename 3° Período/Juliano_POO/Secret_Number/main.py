from random import randint

secret_number = randint(1, 100)

while True:
    number = input("Adivinhe o número: ")

    try:
        number = int(number)
    except:
        print("Desculpe, isso não é um número")
        continue

    if number != secret_number:
        if number > secret_number:
            print (number,  ' é maior que o número secreto')

        elif number < secret_number:
            print (number, ' é menor que o número secreto')

    else:
        print('Você adivinhou o número: ', secret_number)
        break