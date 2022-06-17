print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Maior e Menor valores)":=^138}\033[m')

menor = 1000000
maior = soma = count = 0
n = 'x'
print(f'\n\033[1;30mIniciando programa!!')

while not n == 0:
    n = int(input(f'Digíte um número[digíte 0 para encerrar]: '))
    soma += n
    count += 1
    if n >= 1:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if n == 0:
        count -= 1

media = soma / count
print(f'\nPrograma encerrado!'
      f'\nVocê digitou e somou: \033[32m{count}\033[30m números.'
      f'\nA MÉDIA dos números digitados é: \033[34m{int(media)}\033[30m.'
      f'\nO MAIOR valor digítado foi: \033[35m{maior}\033[30m.'
      f'\nO MENOR valor digítado foi: \033[31m{menor}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
