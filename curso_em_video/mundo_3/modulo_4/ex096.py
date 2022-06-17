def area(largura, comprimento):
    a = comprimento * largura
    print(f'A àrea de um terreno de {largura:.2f} x {comprimento:.2f} é de {a:.2f}m²')


print(f'\n\033[1;30m{"CONTROLE DE TERRENOS":^30}')
print('-' * 30)

L = float(input('LARGURA (m): '))
C = float(input('COMPRIMENTO (m): '))

area(L, C)
