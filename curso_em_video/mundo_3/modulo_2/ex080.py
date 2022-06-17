print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Lista Ordenada Sem Repetições)":=^138}\033[m')

valores = []

print(f'\n\033[1;30mSeja bem vindo!')

for n in range(0, 5):

    while True:
        try:
            if len(valores) > 0:
                x = int(input(f'\nDigite outro número: '))
            else:
                x = int(input(f'\nDigite um número: '))

            if x in valores:
                raise ValueError(f'Este valor já foi inserido, por favor digite outro valor.')
        except ValueError as e:
            print('\033[31mValor inválido\033[30m:', e, end='')
        else:
            break

    if n == 0 or x > valores[-1]:
        valores.append(x)
        print(f'Este valor foi adicionado ao\033[32m final\033[30m da Lista!')
    else:
        pos = 0
        while pos <= len(valores):
            if x < valores[pos]:
                valores.insert(pos, x)
                print(f'Adicionado na posição \033[34m{pos}\033[30m da Lista!')
                break
            pos += 1

print(f'\nOs valores digitados em ordem foram: \033[35m{valores}\033[30m'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
