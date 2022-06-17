print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Validando expressões matematicas)":=^138}\033[m')

x = str(input('\n\033[1;30mDigite sua expressão matematica: '))
lista = []

for simb in x:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print(f'Sua expressão matematica: \033[34m{x}\033[30m , é válida!'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
    print(f'Sua expressão matematica: \033[31m{x}\033[30m , não é válida!'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
