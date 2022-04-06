#!/usr/bin/python3
'''
Formatando valores com modificadores

:s - texto (strings)
:d - inteiro (int)
:f - numero de ponto flutuantes (float)
:.(numero)f - quantidade de casas decimais (float)
:(caracteres) (> ou < ou ^) (Quantidade) (tipo - s, d ou f)
    OBS.: Nesse caso aqui vai preencher tanto na esquerda ou a direita
          ou nos dois lados
> - esquerda
< - direita
^ - centro

.ljust(qtd, valor)
.lower() - tudo minusculo
.upper() - tudo maisculo
.title() - primeiras letras maisculas
'''
nome = 'igor ramalho'
num = 123
print(f'{nome:@<10}')
print(f'{nome:@<20}')
print(f'{nome:@>20}')
print('{:@^20}'.format(nome))
print('{:.2f}'.format(num))
print('{:0<10}'.format(num))
print('{:0>10}'.format(num))
print('{:0^10}'.format(num))
print()
print(nome.center(20, '@'))  # vai preencher nos dois lados
print(nome.rjust(20, '@'))  # vai preencher os lado esquerda
print(nome.ljust(20, '@'))  # vai preencher os lado direito
print()
print(nome.lower())  # tudo minusculos
print(nome.upper())  # tudo maiusculo
print(nome.title())  # As primeiras letras maiusculas
