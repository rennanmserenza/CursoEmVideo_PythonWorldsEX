print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Maior e Menor com Tuplas)":=^138}\033[m')

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'\nOs número sorteados foram: ', end='')

for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior número sorteado foi: {max(numeros)}.'
      f'\nO menor número sorteado foi: {min(numeros)}.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
