print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Times da NBA)":=^138}\033[m')

NBA_leste = ("Bucks", "Raptors", "Celtics", "Pacers", "Heat", "76ers", "Nets", "Magic", "Wizards", "Hornets", "Bulls",
             "Knicks", "Pistons", "Hawks", "Cavaliers")

NBA_oeste = ("Lakers", "Clippers", "Nuggets", "Rockets", "Thunder", "Jazz", "Mavericks", "Trail Blazers", "Grizzlies",
             "Suns", "Spurs", "Kings", "Pelicans", "Timberwolves", "Warriors")

print(f'\n\033[1;30mOs 5 primeiros colocados da NBA da costa Leste são: \033[31m{NBA_leste[0]}\033[30m, '
      f'\033[31m{NBA_leste[1]}\033[30m, \033[31m{NBA_leste[2]}\033[30m, \033[31m{NBA_leste[3]}\033[30m, '
      f'\033[31m{NBA_leste[4]}\033[30m.'
      # f'\033[31m{NBA_leste[0:5]}\033[30m'
      f'\nOs 5 primeiros colocados da NBA da costa Oeste são: \033[32m{NBA_oeste[0]}\033[30m, '
      f'\033[32m{NBA_oeste[1]}\033[30m, \033[32m{NBA_oeste[2]}\033[30m, \033[32m{NBA_oeste[3]}\033[30m, '
      f'\033[32m{NBA_oeste[4]}\033[30m.'
      # f'\033[32m{NBA_oeste[0:5]}\033[30m'
      f'\n\nOs últimos 4 colocados da NBA da costa Leste são: \033[31m{NBA_leste[-1]}\033[30m, '
      f'\033[31m{NBA_leste[-2]}\033[30m, \033[31m{NBA_leste[-3]}\033[30m, \033[31m{NBA_leste[-4]}\033[30m.'
      # f'\033[31m{NBA_leste[-4]}\033[30m'
      f'\nOs últimos 4 colocados da NBA da costa Leste são: \033[32m{NBA_oeste[-1]}\033[30m, '
      f'\033[32m{NBA_oeste[-2]}\033[30m, \033[32m{NBA_oeste[-3]}\033[30m, \033[32m{NBA_oeste[-4]}\033[30m.'
      # f'\033[32m{NBA_oeste[-4:]}\033[30m'
      f'\n\nOs times da costa Leste por ordem alfabética são: \033[31m{sorted(NBA_leste)}\033[30m'
      f'\nOs times da costa Oeste por ordem alfabética são: \033[32m{sorted(NBA_oeste)}\033[30m'
      f'\n\nO Bulls está colocado na tabela na \033[31m{NBA_leste.index("Bulls") + 1}ª\033[30m posição.'
      f'\nO Lakers está colocado na tabela na \033[32m{NBA_oeste.index("Lakers") + 1}ª\033[30m posição.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
