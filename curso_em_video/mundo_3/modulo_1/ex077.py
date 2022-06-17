print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Contando vogais em Tupla)":=^138}\033[m')

words = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalho', 'mercado', 'programador', 'futuro')

for x in words:
    print(f'\n\033[1;30mNa palavra \033[34m{x.upper()}\033[30m temos as vogais: ', end='')
    for letra in x:
        if letra in 'aeiou':
            print(f'\033[31m{letra}', end=' ')

print(f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
