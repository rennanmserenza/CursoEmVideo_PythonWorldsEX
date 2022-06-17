print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Contagem de Pares)":=^138}\033[m')

for n in range(0, 51):
      if n % 2 == 0:
            print(f'\033[1;30m{n}. ', end='')
print('\n')

for n in range(51, 101):
      if n % 2 == 0:
            print(f'\033[36m{n}. ', end='')

print(f'\n\n\033[30;44m{"(Programa Finalizado)":=^138}\033[m')
