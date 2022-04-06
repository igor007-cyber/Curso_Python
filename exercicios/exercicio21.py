#!/usr/bin/python3
import random

p = input('Primeiro Aluno: ')
s = input('Segundo Aluno: ')
t = input('Terceiro Aluno: ')
q = input('Quarto Aluno: ')

lista = [p, s, t, q]
random.shuffle(lista)  # ele embaralha os elementos que está dentro da lista
print(f'A ordem do sortei vai ser essa: {lista}')
