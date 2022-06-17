print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Conversor de Bases Numéricas)":=^138}\033[m')

n = int(input('\n\033[1;30mDigite um número para conversão: '))
b = int(input('Qual base você gostaria de converter:'
              '\n1) binário. 2) octal. 3) Hexadecimal. 0) Todas.'
              '\nSua escolha: '))

if b == 1:
      print(f'\nO número \033[34m{n}\033[30m em Binário equivale a \033[33m{bin(n)[2:]}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')
elif b == 2:
      print(f'\nO número \033[34m{n}\033[30m em Octal equivale a \033[33m{oct(n)[2:]}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')
elif b == 3:
      print(f'\nO número \033[34m{n}\033[30m em Hexadecimal equivale a \033[33m{hex(n)[2:]}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')
elif b == 0:
      print(f'\nO número \033[34m{n}\033[30m convertido em todas as bases equivale a:'
            f'\n\nBinário: \033[35m{bin(n)[2:]}\033[30m.'
            f'\nOctal: \033[35m{oct(n)[2:]}\033[30m.'
            f'\nHexadecimal: \033[35m{hex(n)[2:]}\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')
elif b > 3:
      print(f'Opção inválida reinicie o programa e tente novamente.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')