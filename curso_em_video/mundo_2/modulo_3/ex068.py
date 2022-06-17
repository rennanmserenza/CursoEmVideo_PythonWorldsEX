print(f'\033[1;30;44m{"(Rennan Mendes - Soluções)":=^138}\033[m'
      f'\n\033[1;30;44m{"(Programa Iniciado)":=^138}\033[m'
      f'\n\n\033[1;30;44m{"(Jogo do Par ou Ímpar)":=^138}\033[m')

from random import randint
from time import sleep

count = 0
print('\n\033[1;30mOlá seja bem vindo eu sou \033[35mAurora\033[30m uma I.A. que joga Par ou Ímpar.')
nome = input('\n\033[35mAurora\033[30m: Quem é você?'
             '\nDigite seu nome: ').strip().title().split()

print(f'\n\033[35mAurora\033[30m: Seja Bem Vindo \033[36m{" ".join(nome)}\033[30m, é um prazer conhece-la(o)!'
      f'\n\033[35mAurora\033[30m: Vamos jogar Par ou Ímpar? Acha que ganha de mim \033[36m{nome[0]}\033[30m?\n')

while True:
    try:
        again = input('Aceita jogar[S/N]: ').upper().strip()[0]

        if again.isnumeric() or again not in 'SN':
            raise IndexError('Não te entendi, use apenas S e N.')
    except IndexError as e:
        print('Valor inválido:', e)
    else:
        break

while again == 'S':

    while True:

        print(f'\n{" Rodada {} ":-^100}'.format(count + 1))
        computador = randint(0, 10)
        sleep(1)
        print(f'\n\033[35mAurora\033[30m: Já escolhi que número jogar. Boa sorte \033[36m{nome[0]}\033[30m....')
        sleep(1)

        while True:
            try:
                jogador = int(input(f'\n\033[36m{nome[0]}\033[30m, qual valor você deseja escolher[0 à 10]? '))

                if jogador not in range(0, 11):
                    raise ValueError('Tente um número entre 0 e 10.')
            except ValueError as e:
                print('Valor inválido:', e)
            else:
                break

        while True:
            try:
                escolha = input('Faça sua escolha agora. Par ou Ímpar[P/I]? ').upper().strip()[0]

                if escolha.isnumeric() or escolha not in 'PI':
                    raise IndexError('Não te entendi, use apenas P e I.')
            except IndexError as e:
                print('Valor inválido:', e)
            else:
                break
        sleep(1)

        print(f'\n\033[36m{nome[0]}\033[30m, você escolheu \033[32mPar\033[30m.' if escolha == 'P'
              else f'\n\033[36m{nome[0]}\033[30m, você escolheu \033[32mÍmpar\033[30m.', end=' ')

        print(f'E o número que você escolheu foi: \033[34m{jogador}\033[30m.')
        sleep(2)

        resultado = (computador + jogador) % 2
        print(f'Você escolheu \033[34m{jogador}\033[30m '
              f'e \033[35mAurora\033[30m escolheu \033[31m{computador}\033[30m. '
              f'A soma de seus números é: \033[35m{jogador + computador}\033[30m.')

        if resultado == 0 and escolha == 'P' or resultado == 1 and escolha == 'I':

            if resultado == 0:
                print(f'\nVocê escolheu \033[32mPar\033[30m. E o resultado dessa rodada foi \033[34mPar\033[30m.'
                      f'\n\033[35mAurora\033[30m: \033[32mParabéns \033[36m{nome[0]}\033[30m!!')
            else:
                print(f'\nVocê escolheu \033[32mÍmpar\033[30m. E o resultado dessa rodada foi \033[34mÍmpar\033[30m.'
                      f'\n\n\033[35mAurora\033[30m: \033[32mParabéns \033[36m{nome[0]}\033[30m!!')
            count += 1
            print(f'\n\033[35mAurora\033[30m: \033[36m{nome[0]}\033[30m, '
                  f'você já venceu \033[32m{count}\033[30m rodadas seguidas.')
            while True:
                try:
                    again = input(f'\n\033[35mAurora\033[30m: \033[36m{nome[0]}\033[30m, '
                                  f'gostaria de jogar novamente[S/N]? ').upper().strip()[0]

                    if again.isnumeric() or again not in 'SN':
                        raise IndexError('Não te entendi, use apenas S e N.')
                except IndexError as e:
                    print('Valor inválido:', e)
                else:
                    break
            if again == 'N':
                break

        elif resultado == 1 and escolha == 'P' or resultado == 0 and escolha == 'I':

            if resultado == 0:
                print(f'\nVocê escolheu \033[32mÍmpar\033[30m. E o resultado dessa rodada foi \033[31mPar\033[30m. '
                      f'\n\033[35mAurora\033[30m: \033[31mDesculpa não foi dessa vez.\033[30m'
                      f'\n\n\033[35mAurora\033[30m ganhou dessa vez acontece.')
            else:
                print(f'\nVocê escolheu \033[32mPar\033[30m. E o resultado dessa rodada foi \033[31mÍmpar\033[30m. '
                      f'\n\033[35mAurora\033[30m: \033[31mDesculpa não foi dessa vez.\033[30m'
                      f'\n\n\033[35mAurora\033[30m ganhou dessa vez acontece.')
            break

    if count == 0:
        print(f'\n\033[35mAurora\033[30m: Infelizmente você não ganhou nem uma vez, mais sorte da próxima vez.')
        print('-' * 100)

    elif count <= 5:
        print(f'\n\033[35mAurora\033[30m: Você ganhou \033[33m{count}\033[30m vez(es) seguidas.'
              f'\n\033[35mAurora\033[30m: \033[32mParabéns!!\033[30m')
        print('-' * 100)

    elif count > 5:
        print(f'\n\033[35mAurora\033[30m: Você ganhou \033[34m{count}\033[30m vezes seguidas.'
              f'\n\033[35mAurora\033[30m: \033[34mUow você foi demais!!!\033[30m')
        print('-' * 100)

    while True:
        try:
            again = input(f'\n\033[35mAurora\033[30m: \033[36m{nome[0]}\033[30m, '
                          f'gostaria de jogar novamente[S/N]? ').upper().strip()[0]

            if again.isnumeric() or again not in 'SN':
                raise IndexError('Não te entendi, use apenas S e N.')
        except IndexError as e:
            print('Valor inválido:', e)
        else:
            break

    if again == 'S':
        count = 0

    elif again == 'N':
        print(f'\n\033[35mAurora\033[30m: Tudo bem \033[36m{nome[0]}\033[30m! Obrigado por jogar. '
              f'Estarei te esperando voltar!')

print(f'\033[35mAurora\033[30m: Foi um prazer te-la(o) aqui comigo \033[36m{nome[0]}\033[30m!'
      f'\n\n\033[1;30;44m{"(Programa Finalizado)":=^138}\033[m')
