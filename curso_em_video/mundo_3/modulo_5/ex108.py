from mundo_3.modulo_5.ex108.uteis import moeda


p = float(input(f'\n\033[1;30mDigite o Preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.'
      f'\nO dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.'
      f'\nAumentando 10% temos {moeda.moeda(moeda.aumantar(p, 10))}.'
      f'\nReduzindo 13% temos {moeda.moeda(moeda.diminuir(p, 13))}.')
