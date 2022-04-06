#!/usr/bin/python3

nome = input('Digite o seu primeiro nome: ')
qtd = len(nome)

if qtd <= 4:
    print('Esse nome é curto')
elif qtd <= 6:
    print('Esse nome é normal')
else:
    print('Esse nome é grande')
