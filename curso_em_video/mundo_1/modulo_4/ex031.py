print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m==============(Custo da Viagem)=====================================\033[m')

d = int(input('\n\033[1;30mDigite a ditância que deseja percorrer: '))

if d <= 200:
      print(f'\nO custa da sua viagem de ônibus, para a distância de \033[35m{d}\033[30mkm.'
            f'\nÉ em reais, igual à R$\033[34m{d * 0.5:.2f}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
      print(f'\nO custo da sua viagem de ônibus, para a distância de \033[35m{d}\033[30mkm.'
            f'\nÉ em reais, igual à R$\033[34m{d * 0.45:.2f}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
