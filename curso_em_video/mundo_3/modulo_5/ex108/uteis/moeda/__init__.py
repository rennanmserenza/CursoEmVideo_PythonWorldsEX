def moeda(n=0, local='R$'):
    return f'{local}{n:.2f}'.replace('.', ',')


def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumantar(n=0, percent=0):
    res = n + (n * (percent / 100))
    return res


def diminuir(n=0, percent=0):
    res = n - (n * (percent / 100))
    return res
