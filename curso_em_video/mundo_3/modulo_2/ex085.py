print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Listas com Pares e Ímpares)":=^138}\033[m')

lista_numeros = list()

lista_par = list()
lista_impar = list()

while True:

    lista_numeros.clear()

    for x in range(1, 8):

        while True:
            try:
                y = int(input(f'\n\033[1;30mDigite o {x}º número: '))

                if y in lista_par or y in lista_impar:
                    raise ValueError(f'\033[33mEste valor já foi inserido\033[30m,'
                                     f' por favor digite outro valor.')

            except ValueError as e:
                print('\033[31mValor inválido\033[30m:', e, end='')
            else:
                break
        print('Número inserido com sucesso!')

        if y % 2 == 0:
            lista_par.append(y)
        else:
            lista_impar.append(y)

    lista_par.sort()
    lista_impar.sort()

    lista_numeros.append(lista_par[:])
    lista_numeros.append(lista_impar[:])

    lista_par.clear()
    lista_impar.clear()

    print(f'\nO número PAR digitado foi: ' if len(lista_numeros[0]) == 1
          else '\nOs números PARES digitados foram: ', end='')
    for num in lista_numeros[0]:
        print(f'{num}', end='. ')

    print(f'\nO número ÍMPAR digitado foi: ' if len(lista_numeros[1]) == 1
          else '\nOs números ÍMPARES digitados foram: ', end='')
    for num in lista_numeros[1]:
        print(f'{num}', end='. ')

    while True:
        try:
            again = input(f'\n\nGostaria de continuar\033[34m[S/N]\033[30m? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')
        except IndexError as e:
            print('\033[31mValor inválido\033[30m:', e)
        else:
            break

    if again == 'N':
        break

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
