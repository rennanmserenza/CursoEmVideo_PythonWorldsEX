print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=============(Aumentos multiplos)===================================\033[m')

s = float(input('\n\033[1;30mDigite o valor do seu salário para o reajuste: R$ '))

if s >= 1250.00:
      print(f'\nSeu salário atual é de R$\033[32m{s:.2f}\033[30m.'
            f'\nSeu salário com reajuste de 10% ficará R$\033[33m{s * 1.1:.2f}\033[30m.'
            f'\nSeu aumento salárial foi de: R$\033[34m{s * 0.1:.2f}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
      print(f'\nSeu salário atual é de R$\033[32m{s:.2f}\033[30m.'
            f'\nSeu salário com reajuste de 15% ficará R$\033[33m{s * 1.15:.2f}\033[30m.'
            f'\nSeu aumento salárial foi de: R$\033[34m{s * 0.15:.2f}\033[30m.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
