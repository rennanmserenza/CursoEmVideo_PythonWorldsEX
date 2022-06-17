print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Operações com Matriz em Python)":=^138}\033[m')

from random import randint
from time import sleep

name = str(input(f'\n\033[1;30mOlá seja bem vindo!'
                 f'\nQual seu nome? ')).strip().title().split()

jogo = list()
palpite = list()

while True:

    jogo.clear()
    palpite.clear()

    while True:

        try:
            x = int(input(f'\nQuantos jogos você deseja gerar {name[0]}? '))

        except ValueError as e:
            print('Valor inválido:', e)
        else:
            break

    while len(jogo) < x:

        for n in range(0, 6):
            num = randint(1, 60)

            if num not in palpite:
                palpite.append(num)

            else:
                num += 1
                palpite.append(num)

        palpite.sort()
        jogo.append(palpite[:])
        palpite.clear()

    print(f'-' * 40,
          f'\n{"MEGA SENA":^40}')

    print(f'-' * 40,
          f'\n\n{f"SORTEANDO {x} JOGOS!":=^40}'
          f'\n\n{name[0]} os jogos que você solicitou estão aqui:')

    for n in range(0, x):
        print(f'\nO{n + 1:>3}º jogo é:', end=' ')
        for p in range(0, 6):
            print(f'{jogo[n][p]}, ' if p < 5 else f'{jogo[n][p]}.', end='')
        sleep(1)

    while True:
        try:
            again = input(f'Gostaria de gerar novos números\033[34m[S/N]\033[30m? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')

        except IndexError as e:
            print('\033[31mValor inválido\033[30m:', e)
        else:
            break

    if again == 'N':
        break

print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
