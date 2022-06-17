print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Simulador de Caixa Eletrônico)":=^138}\033[m')

print(f'\n\n\n\n\033[1;30;44m{"=" * 138}\033[m'
      f'\n\n\033[1;30;41m{"(Banco RMS)":^138}\033[m'
      f'\n\n\033[1;30;44m{"=" * 138}\033[m'
      f'\n\n\033[1;30;41m{"Disponibilizamos para nossos clientes cédulas no valor de R$100, R$50, R$20, R$10, R$5, R$2 e R$1.":^138}\033[m')

while True:
    try:
        valor = int(input(f'\033[1;30mQual o valor deseja sacar? R$'))
    except ValueError as e:
        print('Valor inválido:', e)
    else:
        break
total = valor
ced = 100
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'\033[1;30;41m{f"Total de {totalced:^5} cédulas de R${ced:^5}":^138}\033[m')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0
        if total == 0:
            break

print(f'\n\033[1;30;44m{"=" * 138}\033[m'
      f'\n\n\033[1;30;41m{f"Volte sempre, você é sempre bem vindo conosco!":^138}\033[m'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
