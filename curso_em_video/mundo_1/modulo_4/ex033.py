from random import choice

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(Maior e Menor número)==================================\033[m')

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n1 = choice(lista)
lista.remove(n1)
n2 = choice(lista)
lista.remove(n2)
n3 = choice(lista)

print(f'\n\033[1;30mOs números escolhidos foram \033[34m{n1}\033[30m, '
      f'\033[34m{n2}\033[30m e \033[34m{n3}\033[30m.')

if n1 > n2 and n1 > n3:
      print(f'\nO maior número é: \033[32m{n1}\033[30m.')
elif n2 > n1 and n2 > n3:
      print(f'\nO maior número é: \033[32m{n2}\033[30m.')
else:
      print(f'\nO maior número é: \033[32m{n3}\033[30m.')

if n1 < n2 and n1 < n3:
      print(f'O menor número é: \033[31m{n1}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
elif n2 < n1 and n2 < n3:
      print(f'O menor número é: \033[31m{n2}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
      print(f'O menor número é: \033[31m{n3}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
