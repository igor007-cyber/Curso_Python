#!/usr/bin/python3

algo = input('digite algo: ')

print(f'O tipo primitivo dele é {type(algo)} ')
print(f'Ele só tem espaço: {algo.isspace()} ')
print(f'Ele é um numero: {algo.isnumeric()} ')
print(f'Ele é alfabetico: {algo.isalpha()} ')
print(f'Ele é alfanumerico: {algo.isalnum()} ')
print(f'Ele está em maiusculo: {algo.isupper()} ')
print(f'Ele está em minusculo: {algo.islower()} ')
print(f'Ele está capitalizada: {algo.istitle()} ')
# istitle() --> é quando a primeira letra é maiuscula
