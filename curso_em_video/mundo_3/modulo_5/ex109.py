from mundo_3.modulo_5.ex109.uteis.moeda import *

p = float(input(f'\n\033[1;30mDigite o Preço: R$'))
print(f'\nA metade de {moeda(p)} é {metade(p, True)}.'
      f'\nO dobro de {moeda(p)} é {dobro(p, True)}.'
      f'\nAumentando 10% temos {aumantar(p, 10, True)}.'
      f'\nReduzindo 13% temos {diminuir(p, 13, True)}.')
