print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Tratando vários valores v1.0)":=^138}\033[m')


x = int(input(f'\n\033[1;30mDigíte o valor de uma variável para a soma: '))
n = x
soma = x
count = 1

while n != 999:
    x = int(input('Digíte outro valor de variável para a soma[999 para encerrar]: '))
    n = x
    soma += x
    count += 1
    if x == 999:
        soma -= 999
        count -= 1
print(f'\nO número de variáveis digitadas foi \033[34m{count}\033[30m e a soma de todas elas é \033[35m{soma}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
