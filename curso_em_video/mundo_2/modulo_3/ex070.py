print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Estatísticas em produtos)":=^138}\033[m')

total = totalv = total1000 = prodn = prodm = 0

print('\n\033[1;30mOlá seja bem vindo eu sou \033[35mAurora\033[30m uma I.A. criada para te auxiliar.')

nomemain = input('\n\033[35mAurora\033[30m: Quem é você?'
                 '\nDigite seu nome: ').strip().title().split()

while True:
    print('-' * 100)

    if total == 0:
        while True:
            try:
                nome = str(input(f'\033[35mAurora\033[30m: \033[34m{nomemain[0]}\033[30m vamos começar?'
                                 f'\nDigite o nome do produto: ')).strip().title()
                if nome.isnumeric() or nome in '':
                    raise IndexError('Não te entendi, digite apenas nomes nesse campo.')
            except IndexError as e:
                print('Valor inválido:', e)
            else:
                break
    else:
        while True:
            try:
                nome = str(input(f'\033[35mAurora\033[30m: \033[34m{nomemain[0]}\033[30m próximo produto.'
                                 f'\nDigite o nome do produto: ')).strip().title()
                if nome.isnumeric() or nome in '':
                    raise IndexError('Não te entendi, digite apenas nomes nesse campo.')
            except IndexError as e:
                print('Valor inválido:', e)
            else:
                break

    while True:
        try:
            valor = int(input(f'\033[34m{nomemain[0]}\033[30m o produto é: \033[36m{nome}\033[30m, '
                              f'qual o valor deste produto? '))
        except ValueError as e:
            print('Valor inválido:', e)
        else:
            break

    print('-' * 100)

    total += 1
    totalv += valor
    if valor > 1000:
        total1000 += 1

    if total == 1 or valor < prodm:
        prodm = valor
        prodn = nome

    while True:
        try:
            again = input(f'\033[35mAurora\033[30m: Gostaria de inserir mais dados[S/N]? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas S e N.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break

    if again == 'N':
        break

print(f'\n\033[35mAurora\033[30m: \033[34m{nomemain[0]}\033[30m no total foram cadastradas '
      f'\033[36m{total}\033[30m produtos.'
      f'\nO valor da compra é de R$\033[31m{totalv:.2f}\033[30m.'
      f'\nNo total o número de produtos cadastrados a cima de R$1000.00 foi \033[32m{total1000}\033[30m.'
      f'\nO produto mais barato foi \033[35m{prodn}\033[30m e custou R$\033[35m{prodm:.2f}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
