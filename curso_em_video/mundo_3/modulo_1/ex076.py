print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Lista de Preços com Tupla)":=^138}\033[m')

itens = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)

print('\033[1;30m-'*60)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-'*60)

for c in range(0, len(itens), 2):
    print(f'{itens[c]:.<50}R$ {itens[c+1]:>7.2f}')

print('-'*60)
print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
