print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=============(Aluguel de Carros)====================================\033[m')

d = int(input('\n\033[1;30mQuantos dias o carro ficu alugado? dias: '))
km = float(input('Quantos kilometros você percorreu? km: '))
pd = 60 * d
pkm = 0.15 * km
t = (60 * d) + (0.15 * km)

print(f'\nO valor total a pagar pelo alugel do veículo é de R$\033[33m{t:.2f}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
