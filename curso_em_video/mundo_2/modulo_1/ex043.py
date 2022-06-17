print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Calculadora de IMC)":=^138}\033[m')

n = input('\n\033[1;30mOlá, seja bem vindo! Qual seu nome? ').lower().strip().title()
p = float(input(f'\n\033[35m{n}\033[30m quantos quilos você pesa? KG: '))
a = float(input(f'\033[35m{n}\033[30m qual é a sua altura? M: '))

imc = p / (a ** 2)

if imc <= 18.5:
      print(f'\n\033[34m{n}\033[30m analisando sua altura e peso, calculamos o seu \033[33mIMC\033[30m.'
            f'\nSeu IMC é \033[33m{imc:.2f}\033[30m, devido ao seu IMC vemos que você está \033[31mABAIXO\033[30m do peso.'
            f'\nPara chegar no \033[33mIMC ideal\033[30m, seu IMC deve estar entre \033[34m18.6\033[30m e \033[34m25.0\033[30m.'
            f'\nVocê precisa \033[35mGANHAR\033[30m \033[33m{(18.6 - imc) * (a ** 2):.2f}\033[30mKG para estar no \033[35mpeso ideal\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 18.6 <= imc <= 25.0:
      print(f'\n\033[34m{n}\033[30m analisando sua altura e peso, calculamos o seu \033[33mIMC\033[30m.'
            f'\nSeu IMC é \033[34m{imc:.2f}\033[30m, devido ao seu IMC vemos que você está no peso \033[34mIDEAL\033[30m.'
            f'\nPara chegar no IMC ideal, seu IMC deve estar entre 18.6 e 25.0. \033[34mPARABÉNS\033[30m!'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 25.1 <= imc <= 30.0:
      print(f'\n\033[34m{n}\033[30m analisando sua altura e peso, calculamos o seu \033[33mIMC\033[30m.'
            f'\nSeu IMC é \033[33m{imc:.2f}\033[30m, devido ao seu IMC vemos que você está \033[33mACIMA\033[30m do peso.'
            f'\nPara chegar no \033[33mIMC ideal\033[30m, seu IMC deve estar entre \033[34m18.6\033[30m e \033[34m25.0\033[30m.'
            f'\nVocê precisa \033[31mPERDER\033[30m \033[33m{(imc - 21.8) * (a ** 2):.2f}\033[30mKG para estar no \033[35mpeso ideal\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif 30.1 <= imc <= 40.0:
      print(f'\n\033[34m{n}\033[30m analisando sua altura e peso, calculamos o seu \033[33mIMC\033[30m.'
            f'\nSeu IMC é \033[33m{imc:.2f}\033[30m, devido ao seu IMC vemos que sua condição é de \033[33mOBESIDADE\033[30m.'
            f'\nPara chegar no \033[33mIMC ideal\033[30m, seu IMC deve estar entre \033[34m18.6\033[30m e \033[34m25.0\033[30m.'
            f'\nVocê precisa \033[31mPERDER\033[30m \033[33m{(imc - 21.8) * (a ** 2):.2f}\033[30mKG para estar no \033[35mpeso ideal\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
elif imc >= 40.1:
      print(f'\n\033[34m{n}\033[30m analisando sua altura e peso, calculamos o seu \033[33mIMC\033[30m.'
            f'\nSeu IMC é \033[33m{imc:.2f}\033[30m, devido ao seu IMC vemos que sua condição é de \033[33mOBESIDADE MÓRBIDA\033[30m.'
            f'\nPara chegar no \033[33mIMC ideal\033[30m, seu IMC deve estar entre \033[34m18.6\033[30m e \033[34m25.0\033[30m.'
            f'\nVocê precisa \033[31mPERDER\033[30m \033[33m{(imc - 21.8) * (a ** 2):.2f}\033[30mKG para estar no \033[35mpeso ideal\033[30m.'
            f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
