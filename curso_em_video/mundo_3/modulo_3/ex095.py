jogadores = list()
jogador = dict()

while True:

    gols = list()
    gols.clear()

    jogador['nome'] = input('\n\033[1;30mDigite o nome do jogador: ').strip().title()
    n_jogos = int(input(f'digite a quantidade de jogos que {jogador["nome"]} jogou: '))

    for x in range(1, (n_jogos + 1)):
        gols.append(int(input(f'Quantos gols foram marcados no jogo {x}: ')))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:

        again = input('gostaria de cadastrar mais um jogador[S/N]? ').strip().upper()[0]

        if again in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N.')

    print('\n',
          '-' * 60)

    if again == 'N':
        break

print('Nº ', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')

print('\n',
      '-' * 60)

for k, v in enumerate(jogadores):
    print(f'{k:^3}', end=' ')

    for d in v.values():
        print(f'{str(d):<15}', end='')

    print()

print('-' * 60)

while True:

    dados = int(input('\nMostrar dados de qual jogador[digite 999 para encerrar]? '))

    if dados == 999:
        break

    elif dados >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {dados}! Tente outro código.')

    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}:')

        for j in range(1, (len(jogadores[dados]["gols"]) + 1)):
            print(f'    Na {j}ª partida o {jogadores[dados]["nome"]} marcou: {jogadores[dados]["gols"][j - 1]} gols.')
