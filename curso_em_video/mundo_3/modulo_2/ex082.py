print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Dividindo valores em várias Listas)":=^138}\033[m')

valores = []
valorespar = []
valoresimpar = []

while True:

    while True:

        try:
            if len(valores) > 0:
                x = int(input(f'\nDigite outro número: '))
            else:
                x = int(input(f'\n\033[1;30mDigite um número: '))

            if x in valores:
                raise ValueError(f'Este valor já foi inserido, por favor digite outro valor.')

        except ValueError as e:
            print('\033[31mValor inválido\033[30m:', e, end='')
        else:
            break

    if x not in valores:
        valores.append(x)

    if x % 2 == 0 and x not in valorespar:
        valorespar.append(x)
    elif x % 2 == 1 and x not in valoresimpar:
        valoresimpar.append(x)

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

valores.sort()
valorespar.sort()
valoresimpar.sort()

print(f'\nFoi digitado apenas \033[34m1\033[30m valor.' if len(valores) <= 1
      else f'\nForam digitados no total \033[34m{len(valores)}\033[30m valores.',
      f'\nOs valores digitados em ordem crescente foram \033[35m{valores}\033[30m.'
      f'\n\nOs valores \033[34mPar\033[30m digitados em ordem crescente foram \033[34m{valorespar}\033[30m.'
      f'\nOs valores \033[31mÍmpar\033[30m digitados em ordem crescente foram \033[31m{valoresimpar}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
