#!/usr/bin/python3
import math
while True:
    num1 = input('digite um numero: ')
    num2 = input('digite outro numero: ')

    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)

        calculo = input('Qual operação que você quer: "* -> multiplicação", "+ -> soma", "/ -> divisao", "- -> subtração","% -> resto da divisão", "// -> divisão inteira" "** - numero elevado", "r"aiz": ')
        if calculo == '+':
            print(num1 + num2)
        elif calculo == '-':
            assim = input(
                f'voce quer assim {num1} - {num2}, digite "s" ou "n": ')
            if assim == 's' or assim == 'S':
                print(num1 - num2)
            elif assim == 'n' or assim == 'N':
                print(num2 - num1)
            else:
                print('voce digitou errado')
        elif calculo == '*':
            print(num1 * num2)
        elif calculo == '/':
            assim = input(
                f'voce quer assim {num1} / {num2}, digite "s" ou "n": ')
            if assim == 's' or assim == 'S':
                print(num1 / num2)
            elif assim == 'n' or assim == 'N':
                print(num2 / num1)
        elif calculo == '%':
            assim = input(
                f'voce quer assim {num1} % {num2}, digite "s" ou "n": ')
            if assim == 's' or assim == 'S':
                print(num1 % num2)
            elif assim == 'n' or assim == 'N':
                print(num2 % num1)
            else:
                print('voce digitou errado')
        elif calculo == '**':
            assim = input(
                f'voce quer assim {num1} ** {num2}, digite "s" ou "n": ')
            if assim == 's' or assim == 'S':
                print(num1 ** num2)
            elif assim == 'n' or assim == 'N':
                print(num2 ** num1)
            else:
                print('voce digitou errado')
        elif calculo == '//':
            assim = input(
                f'voce quer assim {num1} // {num2}, digite "s" ou "n": ')
            if assim == 's' or assim == 'S':
                print(num1 // num2)
            elif assim == 'n' or assim == 'N':
                print(num2 // num1)
            else:
                print('voce digitou errado')
        elif calculo == 'r':
            assim = input(
                f'voce quer a raiz quadrada do {num1} ou do {num2} ou dos dois, digite 1 ou 2 ou 3: ')
            if assim == '1':
                print(math.sqrt(num1))
            elif assim == '2':
                print(math.sqrt(num2))
            elif assim == '3':
                print(
                    f'A raiz do numero {num1} é {math.sqrt(num1)} e a raiz do numero {num2} é {math.sqrt(num2)}')
            else:
                print('voce digitou errado')
    else:
        print('Digite novamente!!')
