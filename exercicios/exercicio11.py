#!/usr/bin/python3

largura = float(input('digite a largura da parede: '))
altura = float(input('digite a altura da parede: '))
area = altura * largura

print('\nSua parede tem a dimensão de {} x {} e sua area é de {:.2f}m2'.format(
    largura, altura, area))

if area <= 2:
    print('só uma lata resolve')
else:
    print(
        f'Pra {area} metros de area, precisa de {area/2:.2f} latas litros de lata')
