print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Números Primos)":=^138}\033[m')

n = int(input('\n\033[1;30mDigíte um número: '))
print('')
t = 0

for x in range(1, n + 1):
      if n % x == 0:
            print('\033[34m', end='')
            t += 1
      else:
            print('\033[33m', end='')
      print(f'{x}', end='. ')

if t == 2:
      print(f'\n\n\033[30mO número \033[35m{n}\033[30m é \033[34mPRIMO\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
      print(f'\n\n\033[30mO número \033[35m{n}\033[30m é \033[31mNÃO É PRIMO\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
