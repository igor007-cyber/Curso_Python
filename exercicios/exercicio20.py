#!/usr/bin/python3
import random  # Biblioteca de sorteio

p = input('Primeiro Aluno: ')
s = input('Segundo Aluno: ')
t = input('Terceiro Aluno: ')
q = input('Quarto Aluno: ')

lista = [p, q, t, q]
escolha = random.choice(lista)  # Aqui ele escolhe automaticamente

print('O aluno escolhido é {}.'.format(escolha))
