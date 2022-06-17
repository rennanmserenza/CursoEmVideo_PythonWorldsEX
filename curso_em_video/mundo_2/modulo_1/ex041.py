print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Classificando Atletas)":=^138}\033[m')

from datetime import date

n = input('\n\033[1;30mOlá, seja bem vindo! Digíte seu nome: ').lower().strip().title()
a = int(input('Digite em que ano você nasceu: '))

ano = date.today().year
i = ano - a

if i <= 9:
      print(f'\nAnalisando sua idade \033[34m{n}\033[30m, vimos que você tem \033[34m{i}\033[30m anos.'
            f'\nNós estamos te classificando como sendo do grupo \033[34mMIRIN\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 10 <= i <= 14:
      print(f'\nAnalisando sua idade \033[32m{n}\033[30m, vimos que você tem \033[32m{i}\033[30m anos.'
            f'\nNós estamos te classificando como sendo do grupo \033[32mINFANTIL\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 15 <= i <= 19:
      print(f'\nAnalisando sua idade \033[33m{n}\033[30m, vimos que você tem \033[33m{i}\033[30m anos.'
            f'\nNós estamos te classificando como sendo do grupo \033[33mJUNIOR\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 20 <= i <= 29:
      print(f'\nAnalisando sua idade \033[35m{n}\033[30m, vimos que você tem \033[35m{i}\033[30m anos.'
            f'\nNós estamos te classificando como sendo do grupo \033[35mSÊNIOR\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 30 <= i:
      print(f'\nAnalisando sua idade \033[36m{n}\033[30m, vimos que você tem \033[36m{i}\033[30m anos.'
            f'\nNós estamos te classificando como sendo do grupo \033[36mMASTER\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
