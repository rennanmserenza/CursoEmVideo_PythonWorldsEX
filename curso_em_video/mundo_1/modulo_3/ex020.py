from random import shuffle, choice

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m=======(Sorteando uma sequencia em lista)===========================\033[m')

# n = input('\nDigite o nome dos alunos: ')
# lista = n.split()
a1 = input('\n\033[1;30mDigite o nome do primeiro aluno(a): ').title().strip()
a2 = input('Digite o nome do segundo aluno(a): ').title().strip()
a3 = input('Digite o nome do terceiro aluno(a): ').title().strip()
a4 = input('Digite o nome do quarto aluno(a): ').title().strip()
lista = [a1, a2, a3, a4]
# shuffle(lista)
# escolhido = sample(lista, 4)

p = choice(lista)
lista.remove(p)
s = choice(lista)
lista.remove(s)
t = choice(lista)
lista.remove(t)
q = choice(lista)
lista.remove(q)

# print(f'A ordem das apresentações ficou nessa sequência: {lista}.'
#       f'\n\n=============(Programa Finalizado)==================================')

print(f'\nA ordem das apresentações ficou nessa sequência:'
      f'\nO primeiro à apresentar será \033[33m{p}\033[30m.'
      f'\nO segundo a se apresentar será \033[33m{s}\033[30m.'
      f'\nO terceiro a se apresentar será \033[33m{t}\033[30m.'
      f'\nE o quarto a se apresentar será \033[33m{q}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
