from random import randint

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m===============(Par ou ímpar)=======================================\033[m')

n = randint(0, 100)
# n = int(input('\nDigite um número: '))
if n % 2 == 0:
      print(f'\n\033[1;30mO número \033[34m{n}\033[30m é PAR!!'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
      print(f'\n\033[1;30mO número \033[35m{n}\033[30m é ÍMPAR!!'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
