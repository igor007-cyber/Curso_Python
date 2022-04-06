#!/usr/bin/python3

real = input('\ndigite o dinheiro que voce quer converter: R$ ')

if real.isalpha():
    print('voce digitou errado!')
else:
    real = int(real)
    dola = real / 5.45
    euro = real / 6.58

    print(f'\nDe real para dola vai ser: US$ {dola:.2f}')
    print(f'De real para euro vai ser: {euro:.2f}')
