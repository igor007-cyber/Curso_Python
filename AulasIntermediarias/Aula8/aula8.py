'''

Sistema de perguntas e respostas com dicionários em Python

'''

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '4', 'b': '1', 'c': '2', 'd': '3'},
        'resposta_certa': 'a',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5*5?',
        'respostas': {'a': '15', 'b': '20', 'c': '25', 'd': '30'},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 30/2?',
        'respostas': {'a': '15', 'b': '5', 'c': '10', 'd': '12'},
        'resposta_certa': 'a',
    }
}
respostas_certas = 0
print()
for chave_p, chave_v in perguntas.items():
    print(f'{chave_p}: {chave_v["pergunta"]}')

    for resposta_c, resposta_v in chave_v['respostas'].items():
        print(f'[{resposta_c}]: {resposta_v}')
    resposta = input(f'R: ')
    print()
    if resposta == chave_v['resposta_certa']:
        print("Esta correto")
        respostas_certas += 1
    else:
        print('Esta errado')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'Voce acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
