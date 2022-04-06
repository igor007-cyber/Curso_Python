#!/usr/bin/python3

nome = str(input("digite o seu nome: "))
idade = int(input("digite a sua idade: "))
altura = float(input("Digite o sua altura: "))
peso = float(input("Digite o seu peso: "))
anoNacimento = 2021 - idade
imc = peso / (altura**2)

print(f'O seu nome é {nome} e sua idade é {idade} e nasceu no ano de {anoNacimento}, o sua altura é {altura} e seu peso é {peso}. Com isso o seu imc é {imc:.2f}.')
