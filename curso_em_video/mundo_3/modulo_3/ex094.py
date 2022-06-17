pessoas = list()

pessoa = dict()
mulheres = list()

soma_idade = 0

while True:

    pessoa['nome'] = input('\n\033[1;30mDigite o nome a ser cadastrado: ').title().strip()

    while True:

        pessoa['sexo'] = input(f'{pessoa["nome"]} é F ou M: ').upper().strip()[0]

        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor digite apenas M ou F.')

    pessoa['idade'] = int(input(f'Qual é a idade de {pessoa["nome"]}: '))

    soma_idade += pessoa['idade']

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])

    pessoas.append(pessoa.copy())
    while True:

        again = input('Deseja cadastrar mais uma pessoa[S/N]: ').upper().strip()[0]

        if again in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N.')

    if again == 'N':
        break

media_idade = soma_idade / len(pessoas)

print(f'\n',
      f'-=' * 30,
      f'\nA) No total foram cadastradas {len(pessoas)} pessoas.'
      f'\nB) A média de idade é {media_idade:5.2f} anos.'
      f'\nC) As mulheres cadastradas foram {mulheres}.'
      f'\nD) As pessoas à cima da média de idade são: ')

for p in pessoas:
    if p['idade'] >= media_idade:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
