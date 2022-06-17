print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Jogo da Adivinhação v2.0)":=^138}\033[m')

from random import randint
from time import sleep
print('\n\033[1;30mSeja bem vindo! Vamos jogar. Consegue adivinhar em que número estou pensando?')
sleep(2)
print('Já escolhi um número... Tente adivinhar!!')

computador = randint(1, 10)
jogador = 0
count = 0

while jogador != computador:
    jogador = int(input('\nQual número estou pensando? '))
    count += 1

    if jogador > computador:
        print('Você errou, um pouco menos.')
    if jogador < computador:
        print('Voce errou, um pouco mais.')
        print('fala 300 fala 300.')

    if jogador == 300:
        print('Um pouco mais!')
        print('Um pouco mais o que leonidas? 600? 1200? ai já fica 4 pra cada tem q fazer os pirocoptero não sei se da não leonidas.')
    if jogador == 3000:
        print('\n3 mil ai já é de fude leonidas não da não cara. ai é 10 pra cada leonidas não dá não.')
        print('\nÉ leonidas da não cara. Se pra ele não dá já sobra os dele pra mim que ando com ele.')
        print('\nGuerreiros seremos nós contra 30 mil persas!'
              '\n\nO leonidas você tem que parar de arranjar essas briga viado.'
              '\nCabei de noiva velho, a smart fit ainda ta fechada não vai da não.')

print(f'\nPARABÊNS VOCÊ ACERTOU!! Você precisou de \033[34m{count}\033[30m tentativas para acertar.'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
