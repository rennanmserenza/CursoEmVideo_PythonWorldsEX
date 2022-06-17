print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Super Progressão Aritmética v3.0)":=^138}\033[m')

from time import sleep

count = 0
repeat = 'x'

a0 = int(input('\n\033[1;30mDigíte o valor do primeiro termo da P.A.: '))
r = int(input('Digíte o valor da raão da P.A.: '))

while repeat != 0:
    repeat = int(input('\nQuatos termos você gostaria de gerar desta P.A.:'
                       '\n\033[34m[1]\033[30m Mostrar os 10 primeiros.   '
                       '\033[35m[2]\033[30m Mostrar mais.   '
                       '\033[33m[3]\033[30m Entrar com novos valores base.   '
                       '\033[31m[0]\033[30mEncerrar programa.'
                       '\nSelecione sua opção: [0/1/2/3] -> '))
    if repeat == 1:
        print('\nCálculando os 10 primeiros termos da P.A. .....')
        sleep(2)
        while count != 10:
            an = a0 + (count * r)
            count += 1
            print(f'{count} º termo = {an}')
    elif repeat == 2:
        n = int(input('\nAté que termo você gostaria de observar? '))
        while count != n:
            an = a0 + (count * r)
            count += 1
            print(f'{count} º termo = {an}')
    elif repeat == 3:
        print('\n\033[33mEntrando com novos valores!')
        a0 = int(input('\033[30mDigíte o valor do primeiro termo da P.A.: '))
        r = int(input('Digíte o valor da raão da P.A.: '))
        count = 0
    elif repeat == 0:
        print('\nObrigado por testar nosso programa. PROGRAMA ENCERRADO!')
    else:
        print('\nNão entendi qual função você tentou escolher. Tente novamente.')

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
