from time import sleep

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m==========(Penultimo e último nome)=================================\033[m')

nome = str(input('\n\033[1;30mDigite seu nome completo por favor: ')).lower().strip().split()

print(f'\nMuito prazer em te conhecer \033[34m{" ".join(nome).title()}\033[30m!'
      f'\nANALISANDO SEU NOME...')

sleep(2)

print(f'\nSeu primeiro nome é \033[32m{nome[0].capitalize()}\033[30m.'
      f'\nSeu último nome é \033[32m{nome[-1].capitalize()}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
