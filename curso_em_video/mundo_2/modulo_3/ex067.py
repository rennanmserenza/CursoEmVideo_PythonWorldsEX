print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Tabuada v3.0)":=^138}\033[m')

print(f'\n\033[1;30mSeja bem vindo! Vamos criar algumas tabuadas?')
count = 0

while True:
    n = int(input('Digíte o valor de um número para a tabuada: '))
    if n < 1:
        break
    print(f'\nA tabuada de \033[34m{n}\033[30m é:')
    print('-' * 30)
    for x in range(1, 11):
        print(f'\033[34m{n:^3}\033[30m X \033[31m{x:^5}\033[30m = \033[35m{n * x:^5}\033[30m')
    print('-'*30)
    print(f'\nPróxima tabuada!')
    count += 1
print(f'\nNão oferecemos suporte para tabuadas menores que 1.'
      f'\nPrograma encerrado. Você criou \033[35m{count}\033[30m tabuadas.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
