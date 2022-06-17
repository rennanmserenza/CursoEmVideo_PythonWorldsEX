from time import sleep


def contador(partida, fim, passo):

    if passo < 0:
        passo *= (-1)
    if passo == 0:
        passo = 1

    print('\033[1;30m-=' * 30)
    print(f'Contagem de {partida} até {fim} de {passo} em {passo}.')

    if partida < fim:
        for x in range(partida, fim + 1, passo):
            print(x, end=' ')
            sleep(0.4)
        print('FIM')

    else:
        for x in range(partida, fim - 1, - passo):
            print(x, end=' ')
            sleep(0.4)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 30)
print('Agora é com você!')
init = int(input('\nComeça em: '))
end = int(input('Termina em: '))
Passo = int(input('Passo: '))

contador(init, end, Passo)
