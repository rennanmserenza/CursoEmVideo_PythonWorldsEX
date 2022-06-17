print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Grupo da Maioridade)":=^138}\033[m')

print('\n\033[1;30mSejam bem vindos!')

from datetime import date
ano = date.today().year

p = 0
pm = 0

for x in range(1, 8):
      x = int(input('Em que ano você nasceu? '))
      print('')
      i = ano - x
      if i >= 21:
            p += 1
      else:
            pm += 1
print(f'\n\033[34m{p}\033[30m pessoas tem mais de 18 anos. \033[35m{pm}\033[30m pessoas tem menos de 18 anos.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
