print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Análise de dados do grupo)":=^138}\033[m')

count = countm = count18 = countf20 = 0
again = 'S'

print('\n\033[1;30mOlá seja bem vindo eu sou \033[35mAurora\033[30m uma I.A. criada para te auxiliar.')
nomemain = input('\n\033[35mAurora\033[30m: Quem é você?'
                 '\nDigite seu nome: ').strip().title().split()

while again == 'S':
    print('-' * 100)
    if count == 0:
        while True:
            try:
                nome = input(f'\033[35mAurora\033[30m: \033[34m{nomemain[0]}\033[30m vamos começar?'
                             f'\nDigite um nome: ').strip().title()
                if nome.isnumeric():
                    raise IndexError('Não te entendi, digite apenas nomes nesse campo.')
            except IndexError as e:
                print('Valor inválido:', e)
            else:
                break
    else:
        while True:
            try:
                nome = input(f'\n\033[35mAurora\033[30m: \033[36m{nomemain[0]}\033[30m próximo nome.'
                             f'\nDigite um nome: ').strip().title()
                if nome.isnumeric():
                    raise IndexError('Não te entendi, digite apenas nomes nesse campo.')
            except IndexError as e:
                print('Valor inválido:', e)
            else:
                break

    while True:
        try:
            idade = int(input(f'\n\033[36m{nome}\033[30m, qual a idade? '))
        except ValueError as e:
            print('Valor inválido:', e)
        else:
            break

    while True:
        try:
            sexo = input('Qual o sexo[F/M]: ').upper().strip()[0]

            if sexo.isnumeric() or sexo not in 'FM':
                raise IndexError('Não te entendi, use apenas F e M.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break

    print('-' * 100)
    count += 1

    if idade >= 18:
        count18 += 1
    if sexo == 'M':
        countm += 1
    if sexo == 'F' and idade < 20:
        countf20 += 1

    while True:
        try:
            again = input(f'\n\033[35mAurora\033[30m: Gostaria de inserir mais dados[S/N]? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas S e N.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break

    if again == 'N':
        print(f'\n\033[35mAurora\033[30m: \033[34m{nomemain[0]}\033[30m no total foram cadastradas '
              f'\033[36m{count}\033[30m pessoas.'
              f'\nO número de pessoas que tem mais de 18 anos é \033[31m{count18}\033[30m.'
              f'\nO número de homens cadastrados foi \033[32m{countm}\033[30m.'
              f'\nNo total \033[35m{countf20}\033[30m mulheres tem menos de vinte anos de idade.'
              f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
