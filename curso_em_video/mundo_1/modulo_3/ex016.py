from math import trunc

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(Quebrando um Número)===================================\033[m')

num = float(input('\n\033[1;30mDigite um número: '))
# n = trunc(num)

print(f'\nO número é \033[33m{num:.3f}\033[30m, com três casas decimais, e tem como parte inteira \033[33m{trunc(num)}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')

# print(f'O número é {num:.3f}, com três casas decimais, e tem como parte inteira {int(num)}.')
