print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Validaão de Dados)":=^138}\033[m')

sexo = input('\n\033[1;30mDigite aqui qual seu sexo: [F/M] ').strip().upper()[0]
while sexo not in 'HM':
    sexo = input('Não entendi sua resposta. Digite aqui qual seu sexo: [H/M] ').strip().upper()[0]
print(f'\nEntendi sua resposta, seu sexo é \033[34m{sexo}\033[30m.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
