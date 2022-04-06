#!/usr/bin/python3

while True:
    num = input('digite um numero: ')
    num1 = input('digite outro numero: ')
    operador = input('Digite um operador: ')
    sair = input('voce deseja sair: "s" ou "n" = ')

    if sair == 's':
        break

    if not num.isnumeric() or not num1.isnumeric():
        print('digite novamente.')
        continue

    num = int(num)
    num1 = int(num1)

    if operador == "+":
        print(num + num1)
    elif operador == "-":
        print(num - num1)
    elif operador == "*":
        print(num * num1)
    elif operador == "/":
        print(num / num1)
    else:
        print('operador invalido')
