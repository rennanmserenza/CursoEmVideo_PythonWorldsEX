print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Soma de Ímpares e múltiplos de Três)":=^138}\033[m')

soma = 0
cont = 0

for n in range(3, 501, 3):
      if n % 2 == 1:
            soma += n
            cont += 1

print(f'\n\033[1;30mA soma de todos os números ímpares múltiplos de três no intervalo de 1 a 500 é: \033[35m{soma}\033[35m.'
      f'\nUm total de {cont} núumeros'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
