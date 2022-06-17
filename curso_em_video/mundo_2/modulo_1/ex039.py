print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Alistamento Mílitar)":=^138}\033[m')

from datetime import date

n = input('\n\033[1;30mOlá, seja bem vindo! Qual é o seu nome? ').lower().title().strip()
nome = n.split()
a = int(input(f'\033[34m{n}\033[30m, eu poderia saber em que ano você nasceu? '))
m = int(input(f'\033[34m{nome[0]}\033[30m, você já se alistou?'
              f'\n1) Sim.     2) Não.'
              f'\nSua escolha: '))

ano = date.today().year

if ano - a == 18 and m == 1 or ano - a > 18 and m == 1:
    print(f'\nMuito bem \033[34m{n}\033[30m! Vejo aqui que você já se alistou então.'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif ano - a < 18 and m == 2:
    print(f'\n\033[34m{nome[0]}\033[30m você ainda \033[33mNÃO PRECISA\033[30m se alistar. Faltam \033[33m{18 - (ano - a)}\033[30m anos para você se alistar.'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif ano - a == 18 and m == 2:
    print(f'\n\033[34m{n}\033[30m você \033[33mPRECISA\033[30m se alistar este ano. Compareça a uma junta de alistamento milítar o quanto antes.'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif ano - a > 18 and m == 2:
    print(f'\n\033[34m{n}\033[30m \033[33mVOCÊ ESTÁ ATRASADO\033[30m com seu alistamento. Você deveria ter se alistado \033[31m{(ano - a) - 18}\033[30m anos atrás.'
          f'\n\033[34m{nome[0]}\033[30m compareça á uma junta de alistamento milítar o quanto antes.'
          f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
