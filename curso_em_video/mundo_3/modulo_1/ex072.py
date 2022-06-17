print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Número por Extenso)":=^138}\033[m')

nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
        "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    while True:
        try:
            num = int(input(f'\n\033[1;30mDigite um número: '))

            if num > 20 or num < 0:
                raise ValueError('Não entendi. Dígite um número entre 0 e 20.')
        except ValueError as e:
            print('Valor inválido:', e)
        else:
            break

    print(f'Você digitou {nums[num]}.')

    while True:
        try:
            again = input(f'Gostaria de continuar[S/N]? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas S e N.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break
    if again == 'S':
        print('-' * 50)

    if again == 'N':
        break
print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
