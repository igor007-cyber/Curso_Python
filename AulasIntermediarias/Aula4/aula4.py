'''
Funções - def em Python - global - (parte 4)
'''

variavel = "valor"


def func():
    print(variavel)


def func2():
    global variavel  # com isso eu posso mudar a variavel global
    variavel = "outro valor"
    print(variavel)


func()
func2()

print(variavel)
