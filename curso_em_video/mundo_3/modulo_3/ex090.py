print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Dicionário em Python)":=^138}\033[m')

aluno = dict()

aluno['Nome'] = str(input('\n\033[1;30mDigite o nome do aluno: ')).strip().title()
aluno['Média'] = float(input(f'Digite a média de \033[34m{aluno["Nome"]}\033[30m: '))

if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'

elif 5.0 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'

else:
    aluno['Situação'] = 'Reprovado'

print('-' * 40)

for k, v in aluno.items():

    if k == 'Situação':

        if aluno['Situação'] == 'Aprovado':
            print(f'\033[34m{k}\033[30m é \033[32m{v}\033[30m.')

        elif aluno['Situação'] == 'Recuperação':
            print(f'\033[34m{k}\033[30m é \033[31m{v}\033[30m.')

    else:
        print(f'\033[34m{k}\033[30m é \033[30m{v}\033[30m.')

print(f'\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
