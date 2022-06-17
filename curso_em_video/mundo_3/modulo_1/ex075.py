print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Análise de Dados em Tuplas)":=^138}\033[m')

n = (int(input('\n\033[1;30mDigíte o \033[31m1º\033[30m número: ')), int(input('Digíte o \033[31m2º\033[30m número: ')),
     int(input('Digíte o \033[31m3º\033[30m número: ')), int(input('Digíte o \033[31m4º\033[30m número: ')))

if 9 in n:
    repeat = n .count(9)
    print(f'\nO número \033[34m9\033[30m apareceu \033[33m{repeat}\033[30m vezes.')

if 3 in n:
    first = n.index(3)
    print(f'\nO número \033[34m3\033[30m apareceu pela primeira vez na \033[33m{first + 1}º\033[30m posição.')

if n[0] % 2 == 0 or n[1] % 2 == 0 or n[2] % 2 == 0 or n[3] % 2 == 0:
    print(f'\nEstes números digitados são Par:', end=' ')

    for c in n:
        if c % 2 == 0:
            print(f'{c}', end=' ')
else:
    print(f'\nNenhum número \033[33mPAR\033[30m foi digitado!')

print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
