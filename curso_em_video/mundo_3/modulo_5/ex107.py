from mundo_3.modulo_5.ex107.uteis import moeda

p = float(input(f'\n\033[1;30mDigite o Preço: R$'))
print(f'\nA metade de {p} é {moeda.metade(p):.2f}.'
      f'\nO dobro de {p} é {moeda.dobro(p):.2f}.'
      f'\nAumentando 10% de {p} temos {moeda.aumantar(p, 10):.2f}.'
      f'\nReduzindo 13% de {p} temos {moeda.diminuir(p, 13):.2f}.')
