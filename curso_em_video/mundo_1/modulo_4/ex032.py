from datetime import date

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m================(Ano Bissexto)======================================\033[m')

a = int(input('\n\033[1;30mDigite um ano, se quiser que o computador análise o seu ano atual digite 0: '))

if a == 0:
      a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 and a > 1582:
      print(f'\nO ano \033[34m{a}\033[30m é Bissexto visto que:'
            f'\n\nAo dividir por 4 o seu resto é igual a 0.'
            f'\nAo ser dividído por 100 seu resto é maior que 0.'
            f'\nAo ser dividído por 400 seu resto é igual a 0.'
            f'\nE por ser um ano que veio após 1582.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
      print(f'\nO ano \033[34m{a}\033[30m não é Bissexto visto que:'
            f'\n\nAo dividir por 4 o seu resto não é igual a 0.'
            f'\nAo ser dividído por 100 seu resto não é maior que 0.'
            f'\nAo ser dividído por 400 seu resto não é igual a 0.'
            f'\nOu por ser um ano que veio antes de 1582.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
