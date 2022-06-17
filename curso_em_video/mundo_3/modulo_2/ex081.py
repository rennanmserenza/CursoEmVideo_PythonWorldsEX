print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Extraindo dados de uma Lista)":=^138}\033[m')

valores = []
count = x5 = 0

while True:

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

    if x not in valores:
        valores.append(x)
        count += 1

    if x == 5:
        x5 += 1

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

valores.sort(reverse=True)

print(f'\nO valor\033[32m 5\033[30m faz parte da lista!'
      if x5 > 0 else '\nO valor \033[31m5\033[30m não foi encontrado na lista!')

print(f'Foi digitado apenas \033[34m1\033[30m valor.'
      if count <= 1 else f'Foram digitados no total \033[34m{count}\033[30m valores.')

print(f'Os valores digitados em ordem decrescente foram \033[35m{valores}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
