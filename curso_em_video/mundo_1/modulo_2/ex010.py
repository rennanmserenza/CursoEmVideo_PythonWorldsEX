print('\033[1;30;44m============(Rennan Mendes - Soluções)==================================\033[m'
      '\n\033[1;30;44m===============(Programa Iniciado)======================================\033[m'
      '\n\n\033[1;30;44m==============(Investindo em Dolar)=====================================\033[m'
      '\n\n\033[1;33m       Olá seja bem vindo! Vamos investir?'
      '\n   Por favor utilize . para dividir os valores!')

i = float(input('\n\033[30mQuanto você gostaria de investir em dolar? U$: '))
c = float(input('Quanto você possui na carteira? R$: '))

print(f'\nPara investir \033[33m{i:.2f}\033[30m dolares você precisaria,'
      f' no primeiro semestre de 2018, de \033[33m{(i * 3.27):.2f}\033[30m reais.'
      f'\nE no primeiro semestre de 2020 você precisará de \033[33m{(i * 5.24):.2f}\033[30m reais.')

print(f'\nCom o que você possui em carteira em 2020: \033[33m{c:.2f}\033[30m reais.'
      f'\nVocê conseguiria comprar \033[33m{(c / 5.24):.2f}\033[30m dolares.'
      f'\nE em 2018 você conseguiria comprar \033[33m{(c / 3.27):.2f}\033[30m dolares.'
      f'\n\n\033[1;30;44m===============(Programa Finalizado)====================================\033[m')