print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Progressão Aritmética v2.0)":=^138}\033[m')

from time import sleep

count = 0
a0 = int(input('\n\033[1;30mDigíte o valor do primeiro termo da P.A.: '))
r = int(input('Digíte o valor da raão da P.A.: '))
# an = a0
print('\nCálculando os 10 primeiros termos da P.A. .....')
sleep(2)

while count != 10:
    an = a0 + (count * r)
    # an += r
    count += 1
    print(f'{count} º termo = {an}')

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
