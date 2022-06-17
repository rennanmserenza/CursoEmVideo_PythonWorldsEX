print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Analisando Triângulos 2.0)":=^138}\033[m')

r1 = float(input('\n\033[1;30mDigite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
      if r1 == r2 == r3:
            print(f'\nAs retas \033[31mR1\033[30m, \033[34mR2\033[30m e \033[35mR3\033[30m formam um triâmgulo.'
                  f'\nE além disso possuem todos seus valores iguais e formam um triângulo \033[35mEquilátero\033[30m.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif r1 == r2 or r1 == r3 or r2 == r3:
            print(f'\nAs retas \033[31mR1\033[30m, \033[34mR2\033[30m e \033[35mR3\033[30m formam um triâmgulo.'
                  f'\nE além disso possuem ao menos dois dos seus valores iguais e formam um triângulo \033[35mIsóceles\033[30m.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif r1 != r2 != r3:
            print(f'\nAs retas \033[31mR1\033[30m, \033[34mR2\033[30m e \033[35mR3\033[30m formam um triâmgulo.'
                  f'\nE além disso não possuem seus valores iguais e formam um triângulo \033[35mEscaleno\033[30m.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
      print(f'\nAs retas \033[31mR1\033[30m, \033[34mR2\033[30m e \033[35mR3\033[30m não formam um \033[35mtriângulo\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
