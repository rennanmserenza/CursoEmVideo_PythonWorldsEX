from math import cos, sin, tan, radians

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=========(Seno, Cosseno e Tangente)=================================\033[m')

a = float(input('\n\033[1;30mDigite o valor do ângulo: '))

print(f'\nO valor do ângulo é \033[33m{a:.2f}\033[30m°.'
      f'\nSeu seno é equivalente à \033[34m{sin(radians(a)):.2f}\033[30m.'
      f'\nSeu cosseno é igual à \033[34m{cos(radians(a)):.2f}\033[30m.'
      f'\nE sua tangente vale \033[35m{tan(radians(a)):.2f}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
