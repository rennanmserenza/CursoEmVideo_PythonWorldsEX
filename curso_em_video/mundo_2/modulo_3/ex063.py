print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Sequência de Fibonacci v1.0)":=^138}\033[m')

t1 = 0
t2 = 1
count = 3

n = int(input('\n\033[1;30mQuantos números da Sequência de Fibonacci gostaria de ver? '))
print(f'{t1} -> {t2} ', end='')
while count <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    count += 1
    print(f'-> {t3} ', end='')
print('\nSequência encerrada!'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
