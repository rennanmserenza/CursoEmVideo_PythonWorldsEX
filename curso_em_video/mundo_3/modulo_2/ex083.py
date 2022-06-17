print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Validando expressões matemáticas)":=^138}\033[m')

expr = str(input('\n\033[1;30mDigite a expressão matemática que deseja analisar: '))
conjunto = []

for simb in expr:
    if simb == '(':
        conjunto.append('(')
    elif simb == ')':
        if len(conjunto) > 0:
            conjunto.pop()
        else:
            conjunto.append(')')

if len(conjunto) == 0:
    print(f'Sua expressão matemática: \033[34m{expr}\033[30m é válida!'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
    print(f'Sua expressão matemática: \033[31m{expr}\033[30m é inválida!'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
