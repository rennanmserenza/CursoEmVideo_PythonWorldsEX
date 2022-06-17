from time import sleep

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=============(Separando dígitos)====================================\033[m')

n = int(input('\n\033[1;30mDigite um número entre 0 à 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Analizando seu número...')
sleep(3)

print(f'\nUnidade: \033[31m{u}\033[30m.'
      f'\nDezena: \033[32m{d}\033[30m.'
      f'\nCentena: \033[33m{c}\033[30m.'
      f'\nMilhar: \033[34m{m}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
