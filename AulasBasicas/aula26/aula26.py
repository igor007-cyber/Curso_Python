#!/usr/bin/python3

nome = input('Digite o seu nome: ')
print(nome or 'voce nao digitou nada.')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'ian'

variavel = a or b or c or d or e or f or g
print(variavel)
