def fatorial(n, show=False):

    from time import sleep

    """
    ->Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1

    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            sleep(0.4)
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
num = int(input('\n\033[1;30mDigite o valor que deseja: '))
print(fatorial(num, show=True))
print(fatorial(num))
