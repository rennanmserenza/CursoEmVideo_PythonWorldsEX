print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Valores Únicos em Uma Listas)":=^138}\033[m')

valores = []
count = 0

while True:
    if count == 0:

        while True:
            try:
                x = int(input(f'\n\033[1;30mDigite um número: '))

            except ValueError as e:
                print('\033[31mValor inválido\033[30m:', e, end='')
            else:
                break

    else:

        while True:
            try:
                x = int(input(f'\n\033[1;30mDigite outro número: '))

                if x in valores:
                    raise ValueError(f'\033[31mEste valor já foi inserido\033[30m, por favor digite outro valor.')

            except ValueError as e:
                print('\033[31mValor inválido\033[30m:', e, end='')
            else:
                break

    if x not in valores:
        valores.append(x)
        count += 1

    while True:
        try:
            again = input(f'Gostaria de continuar\033[34m[S/N]\033[30m? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break

    if again == 'N':
        break

valores.sort()

print(f'\nOs valores digitados em ordem crescente foram \033[35m{valores}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
