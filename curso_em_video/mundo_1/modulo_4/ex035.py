print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m===========(Analisando Triangulos)==================================\033[m')

r1 = int(input('\n\033[1;30mDigite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceeira reta: '))

if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print(f'\nAs retas R1: \033[32m{r1}\033[30m, R2: \033[34m{r2}\033[30m e R3: \033[35m{r3}\033[30m, formam um triângulo.'
          f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
    print(f'\nAs retas R1: \033[32m{r1}\033[30m, R2: \033[34m{r2}\033[30m e R3: \033[35m{r3}\033[30m, não formam um triângulo.'
          f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
