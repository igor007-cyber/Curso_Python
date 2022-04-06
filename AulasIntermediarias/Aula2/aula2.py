'''
Funções - def em Python - return - (parte 2)
'''


def funcao(var):
    return var
    print('isso nao sera exexutado')


def divisao(n1, n2):
    return n1/n2


def dumb():
    return ('igor', 'ian')


variavel = funcao('Valor que eu quero')
x = divisao(2, 2)

print(x)

if variavel:
    print(variavel)
else:
    print('nenhum valor')

var = dumb()

print(type(var))
