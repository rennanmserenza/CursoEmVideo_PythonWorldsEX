print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Maior e Menor da Sequência)":=^138}\033[m')

maior = 0
menor = 100000000000000000000000

for n in range(0, 5):
      x = float(input('\n\033[1;30mDigite um Peso: '))
      if x > maior:
            maior = x
      if x < menor:
            menor = x
print(f'\nO maior peso digitado foi \033[35m{maior:.2f}\033[30m e o menor peso digitado foi \033[32m{menor:.2f}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
