'''
Funções - def em Python (parte 1)
'''


def saudacao(x, y):
    print(x, y)
    x = x.replace('e', "3")  # ele vai substituir a letra
    print(x)


def funcao(msg):
    print(msg)


saudacao('hello world', 'igor')
funcao(55)
funcao("hello world")
