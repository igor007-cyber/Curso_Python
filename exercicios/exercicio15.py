#!/usr/bin/python3

salario = float(input('Digite o salario do funcionario: '))
salario = float(salario)
aumento = salario * 0.15
total = salario + aumento
print(
    f'O produto  que custava R$ {salario}, na promoção com desconto de 15% vai custar de {total:.2f}')
