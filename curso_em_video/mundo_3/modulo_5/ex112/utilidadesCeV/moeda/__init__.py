def moeda(n=float(0), local='R$'):
    return f'{local}{n:.2f}'.replace('.', ',')


def metade(n=0, formato=False):
    """
    ->Calcula quanto vale a metade de determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se deseja calcular a metade do valor.
    :param formato: quer uma saída formatada?
    :return: o valor da metade calculado com ou sem formatação.
    """
    resto = n / 2
    return resto if formato is False else moeda(resto)


def dobro(n=0, formato=False):
    """
    ->Calcula quanto vale o dobro de determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se deseja calcular o dobro do valor.
    :param formato: quer uma saída formatada?
    :return: o dobro do valor calculado com ou sem formatação.
    """
    resto = n * 2
    return resto if formato is False else moeda(resto)


def aumantar(n=0, percent=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar.
    :param percent: qual é a porcentagem do aumento.
    :param formato: quer uma saída formatada?
    :return: o valor reajustado, com ou sem formatação.
    """
    resto = n + (n * (percent / 100))
    return resto if formato is False else moeda(resto)


def diminuir(n=0, percent=0, formato=False):
    """
    -> Calcula a redução de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar.
    :param percent: qual é a porcentagem da redução.
    :param formato: quer uma saída formatada?
    :return: o valor reajustado, com ou sem formatação.
    """
    resto = n - (n * (percent / 100))
    return resto if formato is False else moeda(resto)


def resumo(n, percent1=10, percent2=5):

    print('-' * 40)
    print(f'RESUMO DO VALOR'.center(40))
    print('-' * 40)

    print(f'Preço Analisado: \t{moeda(n)}'
          f'\nDobro do Preço: \t{dobro(n, True)}'
          f'\nMetade do Preço: \t{metade(n, True)}'
          f'\n{percent1}% de Aumento: \t{aumantar(n, percent1, True)}'
          f'\n{percent2}% de Redução: \t{diminuir(n, percent2, True)}')

    print('-' * 40)
