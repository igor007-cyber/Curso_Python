#!/usr/bin/python3
secreto = input('digite uma palavra: ')
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')

    if chances <= 1:
        print('Voce perdeu')
        break

    if len(letra) > 1:
        print('Ahhh isso nao vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'isso, Tem a letra a {letra}')
    else:
        print(f'nao tem essa letra {letra}')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal voce ganhou!!! a palavra é {secreto_temporario}')
    else:
        print(f'a sua palavra ainda esta assim {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'voce ainda tem {chances} chances')
    print()
