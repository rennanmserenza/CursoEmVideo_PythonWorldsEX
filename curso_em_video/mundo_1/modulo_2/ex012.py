print('\033[1;30;44m=========(Rennan Mendes - Soluções)===============================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)==================================\033[m'
      '\n\n\033[1;30;44m=======(Calcule o desconto do Produto)============================\033[m')

p = float(input('\n\033[1;30mDigite o preço do produto: R$: '))
d = p * (95 / 100)
di = p - d

print(f'\nO preço do produto é \033[33m{p:.2f}\033[30m reais com desconto de 5% ficará: R$\033[33m{d:.2f}\033[30m.'
      f'\nO valor do desconto foi de R$\033[33m{di:.2f}\033[30m.'
      f'\n\n\033[1;30;44m============(Programa Finalizado)==================================\033[m')
