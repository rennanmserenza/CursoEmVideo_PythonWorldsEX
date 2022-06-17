print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=======(Calcule seu ajuste de salário)==============================\033[m')

s = float(input('\n\033[1;30mDigite o valor do seu salário: '))
sn = s * (15 / 100) + s
r = sn - s

print(f'\nSeu salário atual é de \033[33m{s:.2f}\033[30m reais.'
      f'\nSeu salário com reajuste de 15% ficará no valor de \033[33m{sn:.2f}\033[30m reais.'
      f'\nO valor de reajuste é de \033[33m{r:.2f}\033[30m reais.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
