gols = list()
jogador = dict()

soma_gol = 0

jogador['nome'] = input('\n\033[1;39mNome do Jogador: ').title().strip()
n_jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for x in range(1, (n_jogos + 1)):
    g = int(input(f'Quantos gols foram marcados no jogo {x}: '))
    gols.append(g)
    soma_gol += g

jogador['gols'] = gols
jogador['total'] = soma_gol

print('-=' * 30,
      f'\n{jogador}\n',
      '-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} é igual a {v}.')

print('-=' * 30,
      f'\nO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for x in range(1, (n_jogos + 1)):
    print(f'  => Na partida {x}ª {jogador["nome"]} marcou {jogador["gols"][x - 1]}')

print(f'Fez um total de {jogador["total"]} gols.')
