print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Menu de Opções)":=^138}\033[m')

from time import sleep
n1 = int(input('\n\033[1;30mDigite um número: '))
n2 = int(input('Digite outro número: '))

x = 0

while x != 5:
    print('\nSelecione uma das opções a seguir do menu:'
          '\n\033[34m[1] Soma.   [2] Multiplica.   [3] Maior.   [4] Números novos.   [5] Encerrar o programa.\033[30m')
    x = int(input('\nSelecione a opção desejada: '))
    if x == 1:
        soma = n1 + n2
        print(f'A soma de \033[32m{n1}\033[30m e \033[32m{n2}\033[30m é: \033[34m{soma}\033[30m.')
    if x == 2:
        multi = n1 * n2
        print(f'O resultado da multiplicação entre \033[32m{n1}\033[30m e \033[32m{n2}\033[30m é: \033[34m{multi}\033[30m.')
    if x == 3:
        if n1 > n2:
            print(f'O primeiro valor: \033[32m{n1}\033[30m é maior que o segundo valor: \033[32m{n2}\033[30m.')
        elif n1 < n2:
            print(f'O segundo valor: \033[32m{n2}\033[30m é maior que o primeiro valor: \033[32m{n1}\033[30m.')
    if x == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print(f'Estes são seus novos números: \033[32m{n1}\033[30m e \033[32m{n2}\033[30m.')
    sleep(1)
print(f'\033[35mObrigado por testar nosso produto. Volte sempre!\033[30m'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
