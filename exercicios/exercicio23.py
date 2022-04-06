'''
1 - Crie uma função1 que recebe um função2 como parametro e retorne o valor 
da função2 executada
'''

print('***************')
print('QUESTAO 1:')
print('***************')


def func1(x):
    return f'resultado da função2 é: {x}'


def func2(x, z):
    return x + z


print(func1(func2(5, 5)))

########################################################################################
'''
2 - Crie uma função1 que recebe um função2 como parametro e retorne o valor 
da função2 executada. Faça a função1 execultar duas funções que recebam um
numero diferente de argumentos.
'''
print()
print('***************')
print('QUESTAO 2:')
print('***************')


def funcao1(x, nome=None):
    return f'resultado da função2 é: {x} {nome}'


def funcao2(x, z):
    return x + z


print(funcao1(funcao2(10, 5), 'igor'))

###########################################################################################
print("############################")


def mestre(funcao, *args, **kwargs):
    return(funcao(*args, **kwargs))


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


execultando = mestre(fala_oi, 'igor')
execultando2 = mestre(saudacao, 'igor', saudacao='bom dia,')
print(execultando)
print(execultando2)
