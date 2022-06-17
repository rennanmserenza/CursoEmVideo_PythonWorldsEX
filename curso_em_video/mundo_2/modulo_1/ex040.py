print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Cálcule a Média)":=^138}\033[m')

n1 = float(input('\n\033[1;30mDigíte o valor da \033[33mPRIEIRA\033[30m nota: '))
n2 = float(input('Digíte o valor da \033[33mSEGUNDA\033[30m nota:'))

m = (n1 + n2) / 2

if m < 5.0:
      print(f'\nSua média foi \033[31m{m:.2f}\033[30m e por conta dela você foi \033[31mREPROVADO\033[30m. A média de aprovação é acima de 7.0.'
            f'\nFaltou \033[31m{(7.0 - m):.2f}\033[30m pontos para você ser aprovado.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 5.1 <= m <= 6.9:
      print(f'\nSua média foi \033[33m{m:.2f}\033[30m e por conta dela você está de \033[33mRECUPERAÇÃO\033[30m. A média de aprovação é acima de  7.0.'
            f'\nFaltou \033[33m{(7.0 - m):.2f}\033[30m pontos para você ser aprovado.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif m >= 7.0:
      print(f'\nSua média foi \033[34m{m:.2f}\033[30m e por conta dela você foi \033[34mAPROVADO\033[30m. A média de aprovação é acima de 7.0.'
            f'\nVocê foi aprovado com \033[34m{(m - 7.0):.2f}\033[30m pontos a cima da média para ser aprovado.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
