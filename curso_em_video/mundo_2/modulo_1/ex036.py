print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Analisando Empréstimo)":=^138}\033[m')

n = input('\n\n\033[1;30mOlá, seja bem vindo! Qual seu nome? ').lower().title().strip().split()
s = float(input(f'Quanto é a \033[33mRENDA\033[30m mensal do Sr./Sra. \033[34m{n[-1]}\033[30m? R$ '))
e = float(input(f'\nQual o \033[33mVALOR\033[30m do empréstimo que o senhor gostária de solicitar Sr./Sra. \033[34m{n[-1]}\033[30m? '))
t = int(input(f'Sr./Sra. \033[34m{n[-1]}\033[30m, em quantos \033[33mANOS\033[30m o Sr./Sra. gostaria de pagar o empréstimo, (\033[34m5, 6, 7, 8, 9, 10\033[30m)? '))

c = e * (1 + 0.008) ** (t * 12)

if (s * 0.3) > c / (t * 12):
      print(f'\nSr./Sra. \033[34m{n[-1]}\033[30m, o seu empréstimo no valor de R$\033[36m{e:.2f}\033[30m para ser pago no período de \033[33m{t}\033[30m anos foi \033[32mAPROVADO\033[30m.'
            f'\nO valor das parcelas ficou em R$\033[36m{c / (t * 12):.2f}\033[30m ao mês, pelos próximos \033[33m{t}\033[30m anos.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')
else:
      print(
            f'\nSr./Sra. \033[34m{n[-1]}\033[30m, o seu empréstimo no valor de R$\033[36m{e:.2f}\033[30m para ser pago no período de \033[33m{t}\033[30m anos foi \033[31mRECUSADO\033[30m.'
            f'\nO valor das parcelas do empréstimo são superiores à 30% do valor do seu salário Sr.Sra. \033[34m{n[-1]}\033[30m.'
            f'\n\n\033[4mDesculpe-nos mas não poderemos fazer o empréstimo para você\033[1m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^90}\033[m')
