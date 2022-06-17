print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Matriz em Python)":=^138}\033[m')

matriz = list()
linha = list()

print(f'\n\033[1;30mSeja Bem vindo! Vamos montar uma Matriz 3 x 3!')

for x in range(0, 3):

    print(f'\nInsira os valores da \033[33m{x + 1}ª\033[30m Linha:')

    for n in range(0, 3):
        linha.append(int(input(f'Digite o valor na posição \033[33m(\033[34m{x}\033[30m,'
                               f' \033[35m{n}\033[33m)\033[30m: ')))

    matriz.append(linha[:])
    linha.clear()

print(f'\nSua Matriz \033[32m3 x 3\033[30m ficou assim:')

for y in matriz:
    print(f'[{y[0]:^5}] [{y[1]:^5}] [{y[2]:^5}]')

print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
