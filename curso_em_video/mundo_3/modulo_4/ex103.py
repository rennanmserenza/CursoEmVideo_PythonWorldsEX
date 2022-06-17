def ficha(nome='<desconhecido', gol=0):
    print(f'O {nome}, marcou {gol} gols.')


jogador = input('\n\033[1;30mNome do jogador: ').strip().title()
gols = input('Quantos gols foram marcados? ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)

