def moeda(n=float(0), local='R$'):
    return f'{local}{n:.2f}'.replace('.', ',')


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumantar(n=0, percent=0, formato=False):
    res = n + (n * (percent / 100))
    return res if formato is False else moeda(res)


def diminuir(n=0, percent=0, formato=False):
    res = n - (n * (percent / 100))
    return res if formato is False else moeda(res)
