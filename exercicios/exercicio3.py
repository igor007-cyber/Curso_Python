#!/usr/bin/python3

hora = input('digite um numero de 0 a 23 pra dizer em qual hora você está: ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print("O horario de ve estar entre 0 e 23")
    else:
        if hora >= 0 and hora <= 11:
            print('Bom dia')
        elif hora >= 12 and hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Error')
