#!/usr/bin/python3
'''
Iniciar com a letra, pode conter numeros, separar _, letras minusculas

'''

nome = "igor ramalho"
idade = 22
altura = 1.75
e_maior = idade >= 18
peso = 77
imc = peso/(altura**2)

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("E_maior:", e_maior)
print('\n')

# Formas de printar na tela:

print("Meu nome é", nome, 'e eu tenho', idade, "e meu imc é", imc)
# ou
print(f'Meu nome é {nome} e sua idade é {idade} e meu imc é {imc:.2f}')
# formataçao da variaveis com o comando 'f'
# ou
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
# voce pode colocar desse jeito
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(
    n=nome, i=idade, im=imc))
# Dessa forma voce pode colocar em qualquer lugar as variaveis dentro do texto
