from random import choice

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m============(Sorteando com Lista)===================================\033[m')

# n = input('\nDigite o nome dos alunos: ')
# lista = n.split()
a1 = input('\n\033[1;30mDigite o nome do primeiro aluno(a): ').title().strip()
a2 = input('Digite o nome do segundo aluno(a): ').title().strip()
a3 = input('Digite o nome do terceiro aluno(a): ').title().strip()
a4 = input('Digite o nome do quarto aluno(a): ').title().strip()
lista = [a1, a2, a3, a4]
x = choice(lista)

print(f'\nO aluno escolhido para ajuda foi o(a) \033[34m{x}\033[30m.'
      f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
