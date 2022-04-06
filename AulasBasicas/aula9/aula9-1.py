#!/usr/bin/python3

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if idade >= 18 and idade <= 60:
    print(f'O {nome} pode tirar a carteira de motorista.')
else:
    print(f'O {nome} não pode tirar a carteira de motorista.')
