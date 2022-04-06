#!/usr/bin/python3

'''
Operador ternario em Python

'''
logged_user = False
msg = 'usuario logado.' if logged_user else 'usuario nao logado'

print(msg)

idade = input('digite a sua idade: ')
if not idade.isnumeric():
    print('voce precisa digitar só numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    mgse = 'pode acessar' if e_de_maior else 'nao pode acessar'

print(mgse)
"""
if logged_user:
    msg = 'Voce esta logado.'
else:
    msg = 'Voce precisa logar.'

print(msg)
"""
