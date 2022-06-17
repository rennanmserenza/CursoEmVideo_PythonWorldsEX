print('\033[1;30;44m=========(Rennan Mendes - Soluções)==============================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)=================================\033[m'
      '\n\n\033[1;30;44m==============(Vamos converter)==================================\033[m')

m = float(input('\n\033[1;30mEntre a metragem: '))
cm = m * 100
mm = m * 1000
dm = m / 10
hm = m / 100
km = m / 1000

print(f'\n\033[30mO valor em metros é \033[31m{m:.2f}\033[30mm.'
      f'\nem centimetros é \033[32m{cm:.0f}\033[30mcm.'
      f'\nem milimetros é \033[33m{mm:.0f}\033[30mmm.'
      f'\nem decametros é \033[34m{dm:.2f}\033[30mdm.'
      f'\nem hectometros é \033[35m{hm:.2f}\033[30mhm.'
      f'\ne em kilometros é \033[36m{km:.2f}\033[30mkm.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)================================\033[m')
