from random import randint
from time import sleep


def sorteio(lista):

    print('\033[1;30m-' * 30)
    print(f'Os números sorteados foram:')

    for x in range(0, 5):

        r = randint(0, 10)
        sleep(0.4)

        lista.append(r)
        print(f'{r} ', end='')

    print()
    print('-' * 30)


def somaPar(lista):

    soma = 0

    for valor in lista:

        if valor % 2 == 0:
            soma += valor

    print(f'A soma de todos os valores pares de {lista} é: {soma}.')


valores = list()

sorteio(valores)
somaPar(valores)
