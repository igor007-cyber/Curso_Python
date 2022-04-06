#!/usr/bin/python3

produto = input('Qual o preço desse produto? ')
produto = float(produto)
desconto = produto * 0.05
total = produto - desconto
print(
    f'O produto  que custava R$ {produto}, na promoção com desconto de 5% vai custar de {total:.2f}')
