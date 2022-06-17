print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Lista Composta e Analise de Dados)":=^138}\033[m')

pessoas = list()
dados = list()

pesoMA = list()
pesoME = list()

while True:

    while True:

        try:

            if len(pessoas) > 0:
                dados.append(str(input(f'\nDigite outro nome para ser cadastrado: ').title().strip()))

            else:
                dados.append(str(input(f'\n\033[1;30mDigite o nome a ser cadastrado: ').title().strip()))

        except IndexError as e:
            print('\033[31mValor inválido\033[30m:', e)

        else:
            break

    while True:

        try:
            dados.append(float(input(f'Digite o peso de \033[35m{dados[0]}\033[30m: ')))

        except ValueError as e:
            print('\033[31mValor inválido\033[30m:', e)

        else:
            break

    pessoas.append(dados[:])
    dados.clear()

    while True:

        try:
            again = input(f'Gostaria de continuar\033[34m[S/N]\033[30m? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')

        except IndexError as e:
            print('\033[31mValor inválido\033[30m:', e)

        else:
            break

    if again == 'N':
        break

for pos, peso in enumerate(pessoas):

    if peso[1] >= 80:
        pesoMA.append(peso[0])

    elif peso[1] <= 65:
        pesoME.append(peso[0])

print(f'\nNo total foram cadastradas {len(pessoas)}.',

      f'\nAs pessoas à cima da média de peso alta são: {pesoMA}.' if len(pesoMA) > 0
      else f'\nNem uma pessoa à cima da média alta de peso foi cadastrada.',

      f' \nAs pessoas à baixo da média de peso baixo são: {pesoME}.' if len(pesoME) > 0
      else f'\nNem uma pessoa à baixo da média baixa de peso foi cadastrada.',

      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
