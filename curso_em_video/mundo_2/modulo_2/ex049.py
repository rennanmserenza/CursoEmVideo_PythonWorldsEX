print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Tabuada V - 2.0)":=^138}\033[m')

n = int(input('\n\033[1;30mDigite um número: '))
print(f'\nA tabuada de \033[34m{n}\033[30m é: ')

for x in range(1, 11):
      print(f'\033[34m{n:^4}\033[30mx \033[35m{x:^4}\033[30m= \033[36m{(n * x):^2}\033[30m.')

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
