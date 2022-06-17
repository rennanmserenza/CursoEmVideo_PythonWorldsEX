print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Analisador Completo)":=^138}\033[m')

somaIdade = 0
cont = 0
velho = 0
nomeVelho = 'x'

for n in range(1, 5):
    print(f'\n\033[1;30m----------{n}º Pessoa----------')
    nome = str(input('Digite o Seu nome: ')).strip().title()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Digite qual seu sexo: [F/M] ')).strip().upper()[0]
    somaIdade += idade

    while sexo not in 'MF':
        sexo = str(input('Ops não achamos a opção que você digitou. Por favor digite o seu sexo novamente: [F/M] ')).strip().upper()[0]

    if sexo in 'M' and idade > velho:
        velho = idade
        nomeVelho = nome
    if sexo in 'F' and idade <= 20:
        cont += 1

media = somaIdade / 4
print('-'*30)
print(f'\nA média das idades do grupo é \033[34m{int(media)}\033[30m anos.'
      f'\nO homem mais velho é: \033[34m{nomeVelho}\033[30m com \033[3m{velho}\033[30m anos de idade.'
      f'\nO número de mulheres com menos de \033[31m20 anos\033[30m de idade é de \033[31m{cont}\033[30m mulheres.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
