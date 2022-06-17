print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Maior e Menor Valor em Listas)":=^138}\033[m')

valores = []
maior = menor = 0

print(f'\n\033[1;30mSeja bem vindo!\n')

for n in range(0, 5):

    while True:
        try:
            valores.append(int(input(f'Digite um valor para a posição {n}: ')))

        except ValueError as e:
            print('Valor inválido:', e)
        else:
            break

    if n == 0:
        maior = menor = valores[n]
    else:
        if valores[n] > maior:
            maior = valores[n]
        if valores[n] < menor:
            menor = valores[n]

print(f'=-'*30,
      f'\n\nVocê digitou os valores: \033[34m{valores}\033[30m.'
      f'\n\nO menor valor digitado foi \033[35m{min(valores)}\033[30m nas posições: ', end='')

for i, v in enumerate(valores):
    if v == menor:
        print(f'\033[32m{i}\033[30m...', end=' ')

print(f'\nO menor valor digitado foi \033[31m{max(valores)}\033[30m nas posições: ', end='')

for i, v in enumerate(valores):
    if v == maior:
        print(f'\033[32m{i}\033[30m...', end=' ')

print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
