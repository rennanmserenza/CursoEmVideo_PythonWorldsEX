print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=========(Conversor de Temperaturas)================================\033[m')

c = float(input('\n\033[1;30mDigite a temperatura: °C '))

f = (c * 9 / 5) + 32
k = c + 273.15

print(f'\nSua temperatura em Celsius é de \033[32m{c:.2f}\033[30m°C.'
      f'\nSua temperatura em Fahrenheit é de \033[33m{f:.2f}\033[30m°F.'
      f'\nSua temperatura em Kelvin é de \033[35m{k:.2f}\033[30mK.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
