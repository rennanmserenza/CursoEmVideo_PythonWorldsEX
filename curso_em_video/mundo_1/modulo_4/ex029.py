from random import randint

print('\033[1;30;44m=========(Rennan Mendes - Soluções)=================================\033[m'
      '\n\033[1;30;44m=============(Programa Iniciado)====================================\033[m'
      '\n\n\033[1;30;44m==============(Radar Eletrônico)====================================\033[m')

v = randint(40, 150)

if v > 85:
      print(f'\n\033[1;30mVocê foi multado, sua velocidade era de \033[33m{v:.2f}\033[30mkm/h.'
            f'\nVocê estava \033[31m{v - 80:.2f}\033[30mkm/h à cima do limite.'
            f'\nEsta é sua multa, no valor de \033[33m{(v - 80) * 7:.2f}\033[30m reais.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
else:
      print(f'\n\033[1;30mMuito bem você é um cidadão exemplar!'
            f'\nSua velocidade era de \033[32m{v:.2f}\033[30mkm/h.'
            f'\nVocê estava \033[34m{80 - v:.2f}\033[30mkm/h à baixo do limite de velocidade.'
            f'\n\n\033[1;30;44m=============(Programa Finalizado)==================================\033[m')
