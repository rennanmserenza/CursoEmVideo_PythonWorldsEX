print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Vários números com flag)":=^138}\033[m')

soma = count = 0
print('\n\033[1;30mSeja bem vindo!')
while True:
    n = int(input('Digíte um valor[999 para encerrar o programa]: '))
    if n == 999:
        break
    soma += n
    count += 1

print(f'\nNo total foram digítados \033[35m{count}\033[30m números.'
      f'\nA soma de todos os \033[35m{count}\033[30m números é: \033[34m{soma}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
