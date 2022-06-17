print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(jogo de dados  em Python)":=^138}\033[m')

from time import sleep
from random import randint
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}

print('\n\033[1;30mValores Sorteados:\n')

for k, v in jogo.items():
    print(f'{f"{k} tirou {v}.":>20}')
    sleep(1)

print(f'\nO ranking dos jogadores que ganharam é:\n')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{f"O {i + 1}º colocado foi: {v[0]} que tirou {v[1]}.":>50}')
    sleep(1)

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
