print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Somando Pares e Ímpares)":=^138}\033[m')

soma1 = 0
soma2 = 0

for n in range(0, 31):
      if n % 2 == 0:
            soma1 += n
      elif n % 2 == 1:
            soma2 += n

print(f'\n\033[1;30mEm um intervalo de números entre 0 e 30:'
      f'\nA soma de todos os números \033[33mPares\033[30m é: \033[35m{soma1}\033[30m.'
      f'\nA soma de todos os números \033[33mÍmpares\033[30m é: \033[34m{soma2}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
