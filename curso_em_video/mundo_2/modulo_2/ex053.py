print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Invertendo Texto)":=^138}\033[m')

txt = input('\n\033[1;30mDigíte uma frase/palavra: ').lower().strip()

if txt == txt[::-1]:
      print(f'\nA sua frase de trás para frente fica: \033[34m{txt.upper()}\033[30m.'
            f'\nEsta frase/palavra é um \033[33mPALÍNDROMO\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
else:
      print(f'\nA sua frase de trás para frente fica: \033[34m{txt.upper()}\033[30m.'
            f'\nEsta frase/palavra \033[31mNÃO\033[30m é um \033[33mPALÍNDROMO\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
