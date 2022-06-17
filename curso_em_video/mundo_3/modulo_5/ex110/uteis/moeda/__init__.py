def moeda(n=float(0), local='R$'):
    return f'{local}{n:.2f}'.replace('.', ',')


def metade(n=0, formato=False):
    resto = n / 2
    return resto if formato is False else moeda(resto)


def dobro(n=0, formato=False):
    resto = n * 2
    return resto if formato is False else moeda(resto)


def aumantar(n=0, percent=0, formato=False):
    resto = n + (n * (percent / 100))
    return resto if formato is False else moeda(resto)


def diminuir(n=0, percent=0, formato=False):
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
