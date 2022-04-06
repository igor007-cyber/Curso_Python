#!/usr/bin/python3
'''
Entrada de dados

'''
# O input sempre vai retorna string e só.
nome = input("Digite o seu nome: ")
# o tipo dela é uma string e nao um inteiro
idade = input("Digite a sua idade: ")
ano_nacimento = 2021 - int(idade)
print()
print(f"{nome} tem {idade} anos. E nasceu em {ano_nacimento}")
print()
print()

num1 = int(input('Digite um numero: '))
num2 = input('Digite outro numero: ')
num2 = int(num2)
print(num1 ** num2)
