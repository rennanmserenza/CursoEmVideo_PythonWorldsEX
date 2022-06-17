print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Cálculo do Fatorial)":=^138}\033[m')
from time import sleep

f = 1
count = 0
num = int(input('\n\033[1;30mDigíte o valor para cálculo de fatorial: '))
print(f'\nCalculando fatorial de \033[34m{num}!\033[30m = ', end='')
sleep(0.5)

while num > 0:
    print(f'{num}', end='')
    print(' X ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
    count += 1
    sleep(0.6)
print(f'\033[34m{f}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
