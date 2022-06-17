from datetime import date

pessoa = dict()

pessoa['Nome'] = str(input('\n\033[1;30mNome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
pessoa['Idade'] = date.today().year - ano_nascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho[0 se não tiver]: '))

if pessoa['CTPS'] != 0:
    pessoa['Ano Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = int(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Ano Contratação'] + 35) - date.today().year)

print('=' * 80)

for k, v in pessoa.items():
    print(f'  -{k} tem o valor {v}.')
