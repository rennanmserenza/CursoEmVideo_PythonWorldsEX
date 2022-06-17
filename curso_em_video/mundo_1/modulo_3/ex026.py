print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m==========(Ocorrencia de uma letra)=================================\033[m')

frase = str(input('\n\033[1;30mDigite uma frase do seu gosto: ')).strip().lower()
a = frase.count('a')
p = frase.find('a')
u = frase.rfind('a')

print(f'\nA letra "A" apareceu \033[33m{a}\033[30m vezes na sua frase.'
      f'\nA primeira vez que a letra "A" apareceu foi na posição \033[34m{int(p) + 1}\033[30m.'
      f'\nA última vez que a letra "A" apareceu foi na posição \033[34m{u}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')

