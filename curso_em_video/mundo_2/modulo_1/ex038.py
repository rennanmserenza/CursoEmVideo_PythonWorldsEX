print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Comparando Números)":=^138}\033[m')

n1 = int(input('\n\033[1:30mDigíte um número, número_1: '))
n2 = int(input('Digíte outro número, número_2: '))

if n1 > n2:
      print(f'\nO número_1: \033[34m{n1}\033[30m é maior que o número_2: \033[34m{n2}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif n1 < n2:
      print(f'\nO número_2: \033[34m{n2}\033[30m é maior que o número_1: \033[34m{n1}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
      print(f'\nO número_1: \033[34m{n1}\033[30m é igual ao número_2: \033[34m{n2}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
