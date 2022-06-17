print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Operações com Matriz em Python)":=^138}\033[m')

matriz = list()
linha = list()

soma = somaC = maiorL = 0

print(f'\n\033[1;30mSeja Bem vindo! Vamos montar uma Matriz 3 x 3!')

for x in range(0, 3):

    print(f'\nInsira os valores da \033[33m{x + 1}ª\033[30m Linha:')

    for n in range(0, 3):
        a = int(input(f'Digite o valor na posição \033[33m(\033[34m{x}\033[30m,'
                      f' \033[35m{n}\033[33m)\033[30m: '))

        if a % 2 == 0:
            soma += a

        linha.append(a)

    matriz.append(linha[:])
    linha.clear()

for c in range(0, 3):
    if c == 0:
        maiorL = matriz[1][c]
    elif matriz[1][c] > maiorL:
        maiorL = matriz[1][c]

for L in matriz:
    somaC += L[2]

print(f'\n',
      f'-=' * 30,
      f'\nSua Matriz \033[32m3 x 3\033[30m ficou assim:\n')

for y in matriz:
    print(f'[{y[0]:^5}] [{y[1]:^5}] [{y[2]:^5}]')

print(f'\n',
      f'-=' * 30,
      f'\nA soma de todos os valores \033[34mPARES\033[30m inseridos na Matriz é: \033[34m{soma}\033[30m.'
      f'\nA soma de todos os valores da \033[33mTerceira Coluna\033[30m é: \033[33m{somaC}\033[30m.'
      f'\nO maior valor da \033[31mSegunda Linha\033[30m é: \033[31m{maiorL}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
