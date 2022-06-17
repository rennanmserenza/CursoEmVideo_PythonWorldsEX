print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Boletim com Listas Compostas)":=^138}\033[m')

diario = list()
usuario = list()
planilhas = list()

aluno = list()
notas = list()

soma_nota = 0

while True:

    nome = input('\n\033[1;30mOlá seja bem vindo eu sou \033[35mAurora\033[30m e vou te ajudar!'
                 '\n\033[35mAurora\033[30m: Quem é você?'
                 '\nDigite seu nome: ').strip().title().split()

    usuario.append(' '.join(nome))

    planilhas.clear()
    aluno.clear()
    notas.clear()

    while True:

        name = str(input(f'\n\033[35mAurora\033[30m: \033[34m{nome[0]}\033[30m, '
                         f'digite o nome do aluno que deseja inserir.'
                         f'\n\033[35mAurora\033[30m: Nome do aluno: ')).strip().title()

        for x in range(1, 5):

            while True:

                try:
                    nota = int(input(f'Digite a {x}ª nota: '))

                    if nota > 10:
                        raise ValueError(f'Digite um valor entre \033[31m0\033[30m e \033[34m10\033[30m.')

                except ValueError as e:
                    print('\033[35mAurora\033[30m: \033[31mValor inválido\033[30m:', e)

                else:
                    break

            notas.append(nota)

            soma_nota += nota

        media = soma_nota / 4

        aluno.append(name)
        aluno.append(notas[:])
        notas.clear()

        aluno.append(media)
        planilhas.append(aluno[:])
        aluno.clear()

        while True:

            try:
                again = str(input(f'\n\033[35mAurora\033[30m:Gostaria de inserir mais um aluno?'
                                  f'\033[34m[S/N]\033[30m? ')).strip().upper()[0]

                if again.isnumeric() or again not in 'SN':
                    raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')

            except IndexError as e:
                print('\033[35mAurora\033[30m: \033[31mValor inválido\033[30m:', e)

            else:
                break

        if again == 'N':
            break

        else:
            soma_nota = 0

    usuario.append(planilhas[:])
    planilhas.clear()
    diario.append(usuario[:])
    usuario.clear()

    while True:

        try:
            again = str(input(f'\nGostaria de gerar um novo diário\033[34m[S/N]\033[30m? ')).strip().upper()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')

        except IndexError as e:
            print('\033[35mAurora\033[30m: \033[31mValor inválido\033[30m:', e)

        else:
            break

    if again == 'N':
        break

print(f'\n\033[35mAurora\033[30m: Este é o professor que cadastrou alunos no sitema:' if len(diario) == 1
      else f'\n\033[35mAurora\033[30m: Estes são os professores que cadastraram alunos no sitema:',
      f'\n\n')

print(f'-' * 70)

print(f'''\n{f'{"Nº":^8}{"NOME DO PROFESSOR":^40}{"Nº de Alunos":^20}':^70}\n''')

print(f'-' * 70)

for x in range(0, len(diario)):
    print(f'{f"{x + 1:^8}{diario[x][0]:^40}{len(diario[x][1]):^20}":^70}')

print(f'-' * 70)

while True:

    try:
        acesso = str(input(f'\n\033[35mAurora\033[30m: Gostaria de acessar '
                           f'alguma lista de alunos[S/N]? ')).strip().upper()[0]

        if acesso.isnumeric() or acesso not in 'SN':
            raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')

    except IndexError as e:
        print('\033[35mAurora\033[30m: \033[31mValor inválido\033[30m:', e)

    else:
        break

if acesso == 'S':

    print(f'\n\033[35mAurora\033[30m: Qual lista gostaria de acessar?')

    for x in range(0, len(diario)):

        if len(diario) == 1:
            print(f'Lista \033[34m{x + 1}\033[30m do(a) professor(a) \033[34m{diario[x][0]}\033[30m.')

        elif x != (len(diario) - 1):
            print(f'Lista \033[34m{x + 1}\033[30m do(a) professor(a) \033[34m{diario[x][0]}\033[30m, ' if x == 0
                  else f'ou lista \033[34m{x + 1}\033[30m do(a) professor(a) \033[34m{diario[x][0]}\033[30m, ', end='')

        else:
            print(f'ou lista \033[34m{x + 1}\033[30m do(a) professor(a) \033[34m{diario[x][0]}\033[30m.')

    lista_aluno = int(input(f'\nDigite o valor da lista que deseja acessar: '))

    print(f'\n\033[35mAurora\033[30m: Você selecionou a lista do(a) professor(a)'
          f' \033[35m{diario[lista_aluno - 1][0]}\033[30m.'
          
          f'\n\033[35mAurora\033[30m: O(a) professor(a) selecionado(a) '
          f'\033[35m{diario[lista_aluno - 1][0]}\033[30m, '
          f'possui {len(diario[lista_aluno - 1][1])} aluno.' if len(diario[lista_aluno - 1][1]) == 1

          else f'\n\033[35mAurora\033[30m: O(a) professor(a) selecionado(a) '
               f'\033[35m{diario[lista_aluno - 1][0]}\033[30m, '
               f'possui {len(diario[lista_aluno - 1][1])} alunos.')

    print(f'\n',
          f'-' * 80,
          f'''\n{f'{"Nº":^8}{"NOME DO ALUNO":^50}{"Média do Aluno":^20}':^80}\n''',
          f'-' * 80)

    for x in range(0, len(diario[lista_aluno - 1][1])):
        print(f'{f"{x + 1:^8}{diario[lista_aluno - 1][1][x][0]:^50}{diario[lista_aluno - 1][1][x][2]:^20}":^80}')

    while True:

        try:
            acesso_nota = str(input(f'\n\033[35mAurora\033[30m: Gostaria de acessar '
                                    f'algum boletim de aluno[S/N]? ')).strip().upper()[0]

            if acesso.isnumeric() or acesso not in 'SN':
                raise IndexError('Não te entendi, use apenas\033[32m S\033[30m e\033[31m N\033[30m.')

        except IndexError as e:
            print('\033[35mAurora\033[30m: \033[31mValor inválido\033[30m:', e)

        else:
            break

    if acesso_nota == 'S':

        nota_aluno = int(input(f'\n\033[35mAurora\033[30m: Digite o número do aluno que deseja acessar as notas: '))

        print(f'\nAs notas de \033[33m{diario[lista_aluno - 1][1][nota_aluno - 1][0]}\033[30m são:')

        for x in range(0, 4):
            print(f'Nota {x + 1}: {diario[lista_aluno - 1][1][nota_aluno - 1][1][x]:^6.1f}.')

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
