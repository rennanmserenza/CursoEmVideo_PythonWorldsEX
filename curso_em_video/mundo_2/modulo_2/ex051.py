print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Progressão Aritimética)":=^138}\033[m')

a1 = int(input('\n\033[1;30mDigíte o primeiro valor da P.A.: '))
n = int(input('Digíte o número de valores dessa P.A.: '))
r = int(input('Digíte o valor da razão da P.A.: '))
print(''
      '\nOs \033[34m10\033[30m primeiros termos dessa P.A. são:')

a10 = a1 + (11 - 1) * r
an = a1 + (n - 1) * r
sn = (a1 + an) * n / 2

for x in range(a1, a10, r):
      print(f'\033[35m{x}', end='. ')

print(f'\n\n\033[30mA soma de todos os elementos de uma P.A. com \033[34m{n}\033[30m elementos é:'
      f'\n\033[35m{sn:.0f}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
