from math import hypot

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(Catetos e Hipotenusa)==================================\033[m')

co = float(input('\n\033[1;30mDigite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjascente: '))
# hi = (co ** 2 + ca ** 2) ** (1 / 2)

print(f'\nOs catetos valem \033[33m{co:.2f}\033[30m e\033[33m {ca:.2f}\033[30m. O valor de sua hipotenusa é \033[34m{hypot(co, ca):.2f}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')

# print(f'{hi:.2f}')