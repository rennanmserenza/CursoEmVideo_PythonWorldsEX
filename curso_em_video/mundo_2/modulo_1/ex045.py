print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Game: Pedra, Papel, Tesoura)":=^138}\033[m')

from random import choice

n = input('\n\033[1;30mOlá seja bem vindo! Qual é o seu nome? ').lower().title().strip()
print(f'\nOlá, \033[34m{n}\033[30m!')
p1 = int(input(f'\n{n} faça sua escolha:'
               f'\n1) Pedra.        2) Papel.         3) Tesoura.'
               f'\n '))

lista = ['Pedra', 'Papel', 'Tesoura']
p2 = choice(lista)
print(p2)

if (p1 == 1 and p2 == 'Pedra') or (p1 == 2 and p2 == 'Papel') or (p1 == 3 and p2 == 'Tesoura'):
      if p1 == 1:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mPedra\033[30m e o computador escolheu \033[36mPedra\033[30m.'
                  f' Logo vocês \033[33mEMPATARAM\033[30m.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif p1 == 2:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mPapel\033[30m e o computador escolheu \033[36mPapel\033[30m.'
                  f' Logo vocês \033[33mEMPATARAM\033[30m.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif p1 == 3:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mTesoura\033[30m e o computador escolheu \033[36mTesoura\033[30m.'
                  f' Logo vocês \033[33mEMPATARAM\033[30m.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')

elif (p1 == 1 and p2 == 'Tesoura') or (p1 == 2 and p2 == 'Pedra') or (p1 == 3 and p2 == 'Papel'):
      if p1 == 1:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mPedra\033[30m e o computador escolheu \033[36mTesoura\033[30m.'
                  f' Logo você \033[34mVENCEU\033[30m essa rodada.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif p1 == 2:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mPapel\033[30m e o computador escolheu \033[36mPedra\033[30m.'
                  f' Logo você \033[34mVENCEU\033[30m essa rodada.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif p1 == 3:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mTesoura\033[30m e o computador escolheu \033[36mPapel\033[30m.'
                  f' Logo você \033[34mVENCEU\033[30m essa rodada.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')

elif (p1 == 1 and p2 == 'Papel') or (p1 == 1 and p2 == 'Tesoura') or (p1 == 1 and p2 == 'Pedra'):
      if p1 == 1:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mPedra\033[30m e o computador escolheu \033[36mPapel\033[30m.'
                  f' Logo você \033[31mPERDEU\033[30m essa rodada.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif p1 == 2:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mPapel\033[30m e o computador escolheu \033[36mTesoura\033[30m.'
                  f' Logo você \033[31mPERDEU\033[30m essa rodada.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
      elif p1 == 3:
            print(f'\n\033[34m{n}\033[30m você escolheu \033[35mTesoura\033[30m e o computador escolheu \033[36mPedra\033[30m.'
                  f' Logo você \033[31mPERDEU\033[30m essa rodada.'
                  f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
      print('Jogada inválida.')
